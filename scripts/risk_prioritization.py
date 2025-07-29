#!/usr/bin/env python3

import json
from os.path import dirname, abspath, join

ROOT_DIR = dirname(dirname(abspath(__file__)))
TOOL_DIR = join(ROOT_DIR, "scripts")
CHECKLIST_DIR = join(ROOT_DIR, "checklists")

COMPLIANCE_MAPPINGS_FILE = join(TOOL_DIR, "compliance_mappings.json")
CHECKLIST_JSON = join(CHECKLIST_DIR, "compliance_checklist.json")
RISK_REPORT_JSON = join(CHECKLIST_DIR, "risk_prioritization_report.json")

# Risk scoring matrices for each framework
RISK_MATRICES = {
    "IEC_62443": {
        "SL-1": {"priority": 1, "description": "Basic protection against casual or coincidental violation"},
        "SL-2": {"priority": 2, "description": "Protection against intentional violation using simple means"},
        "SL-3": {"priority": 3, "description": "Protection against intentional violation using sophisticated means"},
        "SL-4": {"priority": 4, "description": "Protection against intentional violation using state-of-the-art means"}
    },
    "NIST_CSF": {
        "Identify": {"priority": 1, "description": "Asset management and risk assessment"},
        "Protect": {"priority": 3, "description": "Safeguards to limit impact"},
        "Detect": {"priority": 2, "description": "Identification of cybersecurity events"},
        "Respond": {"priority": 2, "description": "Action regarding detected events"},
        "Recover": {"priority": 1, "description": "Restoration of capabilities"},
        "Govern": {"priority": 2, "description": "Policies and oversight"}
    },
    "EU_RED": {
        "3.3(d)": {"priority": 3, "description": "Network protection - Critical for device operation"},
        "3.3(e)": {"priority": 4, "description": "Personal data protection - Highest privacy impact"},
        "3.3(f)": {"priority": 4, "description": "Financial transaction protection - Highest financial impact"}
    },
    "CATEGORY_PRIORITIES": {
        "Authorization": {"priority": 4, "description": "Access control failures have severe impact"},
        "Information Gathering": {"priority": 2, "description": "Information disclosure moderate risk"},
        "Secrets": {"priority": 4, "description": "Secret exposure critical risk"},
        "Cryptography": {"priority": 4, "description": "Cryptographic failures critical risk"},
        "Configuration and Patch Management": {"priority": 3, "description": "Configuration issues high risk"},
        "Business Logic": {"priority": 3, "description": "Logic flaws high impact"},
        "Input Validation": {"priority": 3, "description": "Injection attacks high risk"},
        "Side-Channel Attacks": {"priority": 3, "description": "Advanced attacks high sophistication"}
    }
}

def load_checklist_data():
    """Load the compliance checklist JSON data"""
    try:
        with open(CHECKLIST_JSON, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {CHECKLIST_JSON} not found. Run create_compliance_checklists.py first.")
        return None

def calculate_test_case_risk(test_case, component_name, category_name):
    """Calculate overall risk score for a test case"""
    scores = []
    
    # Base category score
    category_key = category_name
    if category_key in RISK_MATRICES["CATEGORY_PRIORITIES"]:
        scores.append(RISK_MATRICES["CATEGORY_PRIORITIES"][category_key]["priority"])
    else:
        scores.append(2)  # Default moderate priority
    
    # Framework-specific scoring
    compliance_mappings = test_case.get("compliance_mappings", {})
    
    # IEC 62443 scoring
    iec_mapping = compliance_mappings.get("IEC_62443", {})
    if iec_mapping.get("applicable", True):
        security_level = iec_mapping.get("security_level", "SL-1")
        if security_level in RISK_MATRICES["IEC_62443"]:
            scores.append(RISK_MATRICES["IEC_62443"][security_level]["priority"])
    
    # NIST CSF scoring
    nist_mapping = compliance_mappings.get("NIST_CSF", {})
    functions = nist_mapping.get("functions", [])
    if functions and functions[0] != "To be determined":
        for func in functions:
            if func in RISK_MATRICES["NIST_CSF"]:
                scores.append(RISK_MATRICES["NIST_CSF"][func]["priority"])
                break
    
    # EU RED scoring (highest priority due to regulatory requirements)
    red_mapping = compliance_mappings.get("EU_RED", {})
    if red_mapping.get("applicable", False):
        articles = red_mapping.get("articles", [])
        for article in articles:
            if article in RISK_MATRICES["EU_RED"]:
                scores.append(RISK_MATRICES["EU_RED"][article]["priority"])
                break
        if not articles:
            scores.append(3)  # Default high priority for EU RED applicable tests
    
    # Component-specific adjustments
    component_adjustments = {
        "Processing Units": 1,  # Highest criticality
        "Memory": 1,           # High criticality  
        "Firmware": 1,         # High criticality
        "Data Exchange Services": 0,  # Standard
        "Wireless Interfaces": 1 if red_mapping.get("applicable", False) else 0,  # Higher if wireless
        "Physical Interfaces": 0,   # Standard
        "Internal Interfaces": 0,   # Standard
        "User Interfaces": 0        # Standard
    }
    
    base_score = sum(scores) / len(scores) if scores else 2
    adjustment = component_adjustments.get(component_name, 0)
    final_score = min(4, base_score + adjustment)
    
    return {
        "risk_score": round(final_score, 2),
        "risk_level": get_risk_level(final_score),
        "contributing_factors": {
            "category_priority": RISK_MATRICES["CATEGORY_PRIORITIES"].get(category_key, {}).get("priority", 2),
            "component_adjustment": adjustment,
            "framework_scores": {
                "iec_62443": iec_mapping.get("security_level", "N/A") if iec_mapping.get("applicable", True) else "N/A",
                "nist_csf": functions[0] if functions and functions[0] != "To be determined" else "N/A",
                "eu_red": "Applicable" if red_mapping.get("applicable", False) else "N/A"
            }
        }
    }

def get_risk_level(score):
    """Convert numeric score to risk level"""
    if score >= 3.5:
        return "Critical"
    elif score >= 2.5:
        return "High"
    elif score >= 1.5:
        return "Medium"
    else:
        return "Low"

def generate_risk_prioritization_report(data):
    """Generate comprehensive risk prioritization report"""
    report = {
        "metadata": {
            "title": "OWASP ISTG Risk Prioritization Report",
            "description": "Risk-based prioritization of IoT security test cases across compliance frameworks",
            "frameworks_analyzed": ["IEC 62443", "NIST CSF 2.0", "EU RED", "EU CRA/ETSI"],
            "risk_methodology": "Multi-factor analysis based on compliance framework priorities and component criticality"
        },
        "risk_summary": {
            "critical": [],
            "high": [],
            "medium": [],
            "low": []
        },
        "framework_analysis": {
            "IEC_62443": {"test_cases": [], "avg_security_level": 0},
            "NIST_CSF": {"test_cases": [], "function_distribution": {}},
            "EU_RED": {"test_cases": [], "applicable_count": 0},
            "EU_CRA_ETSI": {"test_cases": [], "requirement_coverage": {}}
        },
        "component_analysis": {},
        "prioritized_test_cases": []
    }
    
    all_test_cases = []
    
    # Extract all test cases with risk calculations
    for component_id in data:
        if component_id == "compliance_frameworks":
            continue
            
        component = data[component_id]
        component_name = component.get("title", component_id)
        
        # Initialize component analysis
        report["component_analysis"][component_name] = {
            "total_tests": 0,
            "risk_distribution": {"Critical": 0, "High": 0, "Medium": 0, "Low": 0},
            "compliance_coverage": {}
        }
        
        # Process main categories
        if "categories" in component:
            for category_id in component["categories"]:
                category = component["categories"][category_id]
                category_name = category.get("title", category_id)
                
                if "test_cases" in category:
                    for test_id in category["test_cases"]:
                        test_case = category["test_cases"][test_id]
                        
                        # Calculate risk
                        risk_data = calculate_test_case_risk(test_case, component_name, category_name)
                        
                        # Create enhanced test case record
                        enhanced_test = {
                            "id": test_id,
                            "title": test_case.get("title", ""),
                            "component": component_name,
                            "category": category_name,
                            "risk_score": risk_data["risk_score"],
                            "risk_level": risk_data["risk_level"],
                            "contributing_factors": risk_data["contributing_factors"],
                            "compliance_mappings": test_case.get("compliance_mappings", {})
                        }
                        
                        all_test_cases.append(enhanced_test)
                        
                        # Update component analysis
                        report["component_analysis"][component_name]["total_tests"] += 1
                        report["component_analysis"][component_name]["risk_distribution"][risk_data["risk_level"]] += 1
        
        # Process specializations
        if "specializations" in component:
            for spec_id in component["specializations"]:
                spec = component["specializations"][spec_id]
                spec_name = spec.get("title", spec_id)
                
                if spec_name not in report["component_analysis"]:
                    report["component_analysis"][spec_name] = {
                        "total_tests": 0,
                        "risk_distribution": {"Critical": 0, "High": 0, "Medium": 0, "Low": 0},
                        "compliance_coverage": {}
                    }
                
                if "categories" in spec:
                    for category_id in spec["categories"]:
                        category = spec["categories"][category_id]
                        category_name = category.get("title", category_id)
                        
                        if "test_cases" in category:
                            for test_id in category["test_cases"]:
                                test_case = category["test_cases"][test_id]
                                
                                # Calculate risk
                                risk_data = calculate_test_case_risk(test_case, spec_name, category_name)
                                
                                # Create enhanced test case record
                                enhanced_test = {
                                    "id": test_id,
                                    "title": test_case.get("title", ""),
                                    "component": spec_name,
                                    "category": category_name,
                                    "risk_score": risk_data["risk_score"],
                                    "risk_level": risk_data["risk_level"],
                                    "contributing_factors": risk_data["contributing_factors"],
                                    "compliance_mappings": test_case.get("compliance_mappings", {})
                                }
                                
                                all_test_cases.append(enhanced_test)
                                
                                # Update component analysis
                                report["component_analysis"][spec_name]["total_tests"] += 1
                                report["component_analysis"][spec_name]["risk_distribution"][risk_data["risk_level"]] += 1
    
    # Sort test cases by risk score (highest first)
    all_test_cases.sort(key=lambda x: x["risk_score"], reverse=True)
    report["prioritized_test_cases"] = all_test_cases
    
    # Populate risk summary
    for test_case in all_test_cases:
        risk_level = test_case["risk_level"]
        report["risk_summary"][risk_level.lower()].append({
            "id": test_case["id"],
            "title": test_case["title"],
            "component": test_case["component"],
            "risk_score": test_case["risk_score"]
        })
    
    # Generate framework analysis
    for test_case in all_test_cases:
        mappings = test_case["compliance_mappings"]
        
        # IEC 62443 analysis
        iec_mapping = mappings.get("IEC_62443", {})
        if iec_mapping.get("applicable", True):
            report["framework_analysis"]["IEC_62443"]["test_cases"].append(test_case["id"])
        
        # NIST CSF analysis
        nist_mapping = mappings.get("NIST_CSF", {})
        functions = nist_mapping.get("functions", [])
        if functions and functions[0] != "To be determined":
            report["framework_analysis"]["NIST_CSF"]["test_cases"].append(test_case["id"])
            for func in functions:
                if func in report["framework_analysis"]["NIST_CSF"]["function_distribution"]:
                    report["framework_analysis"]["NIST_CSF"]["function_distribution"][func] += 1
                else:
                    report["framework_analysis"]["NIST_CSF"]["function_distribution"][func] = 1
        
        # EU RED analysis
        red_mapping = mappings.get("EU_RED", {})
        if red_mapping.get("applicable", False):
            report["framework_analysis"]["EU_RED"]["test_cases"].append(test_case["id"])
            report["framework_analysis"]["EU_RED"]["applicable_count"] += 1
        
        # EU CRA/ETSI analysis
        cra_mapping = mappings.get("EU_CRA_ETSI", {})
        requirements = cra_mapping.get("essential_requirements", [])
        if requirements and requirements[0] != "To be determined":
            report["framework_analysis"]["EU_CRA_ETSI"]["test_cases"].append(test_case["id"])
    
    return report

def export_risk_report(report, output_file=RISK_REPORT_JSON):
    """Export risk prioritization report as JSON"""
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Risk prioritization report exported to: {output_file}")

def print_risk_summary(report):
    """Print a summary of risk prioritization results"""
    print("\n" + "="*60)
    print("OWASP ISTG RISK PRIORITIZATION SUMMARY")
    print("="*60)
    
    print(f"\nTotal Test Cases Analyzed: {len(report['prioritized_test_cases'])}")
    
    print("\nRisk Level Distribution:")
    for level in ["critical", "high", "medium", "low"]:
        count = len(report["risk_summary"][level])
        percentage = (count / len(report['prioritized_test_cases']) * 100) if report['prioritized_test_cases'] else 0
        print(f"  {level.title()}: {count} ({percentage:.1f}%)")
    
    print("\nTop 10 Highest Risk Test Cases:")
    for i, test_case in enumerate(report["prioritized_test_cases"][:10], 1):
        print(f"  {i:2d}. {test_case['id']} - {test_case['title'][:50]}...")
        print(f"      Risk: {test_case['risk_level']} ({test_case['risk_score']:.2f}) | Component: {test_case['component']}")
    
    print("\nFramework Coverage:")
    for framework, data in report["framework_analysis"].items():
        if framework == "EU_RED":
            applicable = data["applicable_count"]
            total = len(report['prioritized_test_cases'])
            print(f"  {framework}: {applicable}/{total} test cases applicable ({applicable/total*100:.1f}%)")
        else:
            covered = len(data["test_cases"])
            total = len(report['prioritized_test_cases'])
            print(f"  {framework}: {covered}/{total} test cases covered ({covered/total*100:.1f}%)")

def main():
    """Main function to generate risk prioritization report"""
    print("Loading compliance checklist data...")
    data = load_checklist_data()
    
    if not data:
        return
    
    print("Calculating risk scores for all test cases...")
    report = generate_risk_prioritization_report(data)
    
    print("Exporting risk prioritization report...")
    export_risk_report(report)
    
    print_risk_summary(report)
    
    print(f"\nDetailed report available at: {RISK_REPORT_JSON}")

if __name__ == "__main__":
    main()
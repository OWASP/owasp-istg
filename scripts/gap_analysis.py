#!/usr/bin/env python3

import json
from os.path import dirname, abspath, join
from collections import defaultdict

ROOT_DIR = dirname(dirname(abspath(__file__)))
TOOL_DIR = join(ROOT_DIR, "scripts")
CHECKLIST_DIR = join(ROOT_DIR, "checklists")

COMPLIANCE_MAPPINGS_FILE = join(TOOL_DIR, "compliance_mappings.json")
CHECKLIST_JSON = join(CHECKLIST_DIR, "compliance_checklist.json")
GAP_ANALYSIS_JSON = join(CHECKLIST_DIR, "gap_analysis_report.json")

def load_data():
    """Load compliance checklist data"""
    try:
        with open(CHECKLIST_JSON, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {CHECKLIST_JSON} not found. Run create_compliance_checklists.py first.")
        return None

def extract_test_cases(data):
    """Extract all test cases with their compliance mappings"""
    test_cases = []
    
    for component_id in data:
        if component_id == "compliance_frameworks":
            continue
            
        component = data[component_id]
        
        # Process main categories
        if "categories" in component:
            for category_id in component["categories"]:
                category = component["categories"][category_id]
                if "test_cases" in category:
                    for test_id in category["test_cases"]:
                        test_case = category["test_cases"][test_id]
                        test_cases.append({
                            "id": test_id,
                            "title": test_case.get("title", ""),
                            "component": component.get("title", component_id),
                            "category": category.get("title", category_id),
                            "compliance_mappings": test_case.get("compliance_mappings", {})
                        })
        
        # Process specializations  
        if "specializations" in component:
            for spec_id in component["specializations"]:
                spec = component["specializations"][spec_id]
                if "categories" in spec:
                    for category_id in spec["categories"]:
                        category = spec["categories"][category_id]
                        if "test_cases" in category:
                            for test_id in category["test_cases"]:
                                test_case = category["test_cases"][test_id]
                                test_cases.append({
                                    "id": test_id,
                                    "title": test_case.get("title", ""),
                                    "component": spec.get("title", spec_id),
                                    "category": category.get("title", category_id),
                                    "compliance_mappings": test_case.get("compliance_mappings", {})
                                })
    
    return test_cases

def analyze_framework_coverage(test_cases):
    """Analyze coverage for each compliance framework"""
    frameworks = ["IEC_62443", "NIST_CSF", "EU_RED", "EU_CRA_ETSI"]
    
    coverage_analysis = {
        "framework_coverage": {},
        "cross_framework_mapping": {},
        "coverage_gaps": {},
        "overlapping_requirements": {}
    }
    
    for framework in frameworks:
        covered_tests = []
        applicable_tests = []
        not_applicable_tests = []
        tbd_tests = []
        
        for test_case in test_cases:
            mapping = test_case["compliance_mappings"].get(framework, {})
            
            if not mapping:
                tbd_tests.append(test_case["id"])
            elif mapping.get("applicable", True) == False:
                not_applicable_tests.append(test_case["id"])
            elif has_meaningful_mapping(mapping, framework):
                covered_tests.append(test_case["id"])
                applicable_tests.append(test_case["id"])
            else:
                tbd_tests.append(test_case["id"])
                applicable_tests.append(test_case["id"])
        
        total_applicable = len(applicable_tests) + len(tbd_tests)
        coverage_percentage = (len(covered_tests) / total_applicable * 100) if total_applicable > 0 else 0
        
        coverage_analysis["framework_coverage"][framework] = {
            "total_test_cases": len(test_cases),
            "applicable_test_cases": total_applicable,
            "covered_test_cases": len(covered_tests),
            "not_applicable_test_cases": len(not_applicable_tests),
            "tbd_test_cases": len(tbd_tests),
            "coverage_percentage": round(coverage_percentage, 2),
            "covered_tests": covered_tests,
            "tbd_tests": tbd_tests,
            "not_applicable_tests": not_applicable_tests
        }
    
    return coverage_analysis

def has_meaningful_mapping(mapping, framework):
    """Check if a mapping has meaningful content (not just TBD)"""
    if not mapping:
        return False
        
    # Convert mapping to string and check for placeholder content
    mapping_str = json.dumps(mapping).lower()
    
    if "to be determined" in mapping_str or "tbd" in mapping_str:
        return False
        
    # Framework-specific checks
    if framework == "IEC_62443":
        return mapping.get("security_level") not in [None, "TBD", "To be determined"]
    elif framework == "NIST_CSF":
        functions = mapping.get("functions", [])
        return functions and functions[0] not in ["To be determined", "TBD"]
    elif framework == "EU_RED":
        return mapping.get("applicable", False) == True
    elif framework == "EU_CRA_ETSI":
        requirements = mapping.get("essential_requirements", [])
        return requirements and requirements[0] not in ["To be determined", "TBD"]
    
    return True

def analyze_cross_framework_overlaps(test_cases):
    """Analyze overlapping requirements across frameworks"""
    overlaps = {
        "multi_framework_tests": [],
        "framework_pairs": {
            "IEC_62443_NIST_CSF": [],
            "IEC_62443_EU_RED": [],
            "IEC_62443_EU_CRA_ETSI": [],
            "NIST_CSF_EU_RED": [],
            "NIST_CSF_EU_CRA_ETSI": [],
            "EU_RED_EU_CRA_ETSI": []
        },
        "all_frameworks": []
    }
    
    for test_case in test_cases:
        mappings = test_case["compliance_mappings"]
        applicable_frameworks = []
        
        for framework in ["IEC_62443", "NIST_CSF", "EU_RED", "EU_CRA_ETSI"]:
            mapping = mappings.get(framework, {})
            if mapping and (mapping.get("applicable", True) != False) and has_meaningful_mapping(mapping, framework):
                applicable_frameworks.append(framework)
        
        if len(applicable_frameworks) > 1:
            test_info = {
                "id": test_case["id"],
                "title": test_case["title"],
                "component": test_case["component"],
                "frameworks": applicable_frameworks
            }
            overlaps["multi_framework_tests"].append(test_info)
            
            if len(applicable_frameworks) == 4:
                overlaps["all_frameworks"].append(test_info)
            
            # Check pair combinations
            frameworks = applicable_frameworks
            for i in range(len(frameworks)):
                for j in range(i + 1, len(frameworks)):
                    pair_key = f"{frameworks[i]}_{frameworks[j]}"
                    if pair_key in overlaps["framework_pairs"]:
                        overlaps["framework_pairs"][pair_key].append(test_info["id"])
    
    return overlaps

def identify_coverage_gaps(test_cases):
    """Identify gaps in compliance coverage"""
    gaps = {
        "unmapped_tests": [],
        "framework_specific_gaps": {},
        "critical_gaps": [],
        "recommendations": []
    }
    
    frameworks = ["IEC_62443", "NIST_CSF", "EU_RED", "EU_CRA_ETSI"]
    
    for framework in frameworks:
        framework_gaps = []
        
        for test_case in test_cases:
            mapping = test_case["compliance_mappings"].get(framework, {})
            
            if not mapping or not has_meaningful_mapping(mapping, framework):
                if mapping.get("applicable", True) != False:  # Skip if explicitly not applicable
                    framework_gaps.append({
                        "id": test_case["id"],
                        "title": test_case["title"],
                        "component": test_case["component"],
                        "category": test_case["category"]
                    })
        
        gaps["framework_specific_gaps"][framework] = framework_gaps
    
    # Identify completely unmapped tests
    for test_case in test_cases:
        mappings = test_case["compliance_mappings"]
        has_any_mapping = False
        
        for framework in frameworks:
            mapping = mappings.get(framework, {})
            if mapping and has_meaningful_mapping(mapping, framework):
                has_any_mapping = True
                break
        
        if not has_any_mapping:
            gaps["unmapped_tests"].append({
                "id": test_case["id"],
                "title": test_case["title"],
                "component": test_case["component"],
                "category": test_case["category"]
            })
    
    # Identify critical gaps (high-risk test cases without proper mapping)
    critical_categories = ["Authorization", "Secrets", "Cryptography"]
    critical_components = ["Processing Units", "Memory", "Firmware"]
    
    for test_case in test_cases:
        if (test_case["category"] in critical_categories or 
            test_case["component"] in critical_components):
            
            mappings = test_case["compliance_mappings"]
            well_mapped = 0
            
            for framework in frameworks:
                mapping = mappings.get(framework, {})
                if mapping and has_meaningful_mapping(mapping, framework):
                    well_mapped += 1
            
            if well_mapped < 2:  # Critical test cases should map to at least 2 frameworks
                gaps["critical_gaps"].append({
                    "id": test_case["id"],
                    "title": test_case["title"],
                    "component": test_case["component"],
                    "category": test_case["category"],
                    "mapped_frameworks": well_mapped
                })
    
    return gaps

def generate_recommendations(coverage_analysis, overlaps, gaps):
    """Generate recommendations for improving compliance coverage"""
    recommendations = {
        "priority_actions": [],
        "framework_specific": {},
        "general_improvements": []
    }
    
    # Priority actions based on critical gaps
    if gaps["critical_gaps"]:
        recommendations["priority_actions"].append({
            "action": "Map critical security test cases",
            "description": f"Complete compliance mappings for {len(gaps['critical_gaps'])} critical test cases",
            "test_cases": [gap["id"] for gap in gaps["critical_gaps"]],
            "urgency": "High"
        })
    
    # Framework-specific recommendations
    for framework, coverage in coverage_analysis["framework_coverage"].items():
        framework_recs = []
        
        if coverage["coverage_percentage"] < 50:
            framework_recs.append({
                "action": "Improve framework coverage",
                "description": f"Coverage is only {coverage['coverage_percentage']:.1f}%. Map {len(coverage['tbd_tests'])} pending test cases.",
                "priority": "High"
            })
        
        if coverage["tbd_tests"]:
            framework_recs.append({
                "action": "Complete TBD mappings",
                "description": f"Complete {len(coverage['tbd_tests'])} To-be-determined mappings",
                "test_cases": coverage["tbd_tests"][:10],  # Show first 10
                "priority": "Medium"
            })
        
        recommendations["framework_specific"][framework] = framework_recs
    
    # General improvements
    if overlaps["multi_framework_tests"]:
        recommendations["general_improvements"].append({
            "action": "Leverage cross-framework synergies",
            "description": f"{len(overlaps['multi_framework_tests'])} test cases map to multiple frameworks. Use these for efficient multi-compliance testing.",
            "benefit": "Cost-effective compliance across multiple regulations"
        })
    
    if len(overlaps["all_frameworks"]) < 10:
        recommendations["general_improvements"].append({
            "action": "Increase universal test coverage",
            "description": f"Only {len(overlaps['all_frameworks'])} test cases cover all frameworks. Identify more universal security requirements.",
            "benefit": "Comprehensive security baseline across all regulations"
        })
    
    return recommendations

def generate_gap_analysis_report(data):
    """Generate comprehensive gap analysis report"""
    test_cases = extract_test_cases(data)
    
    report = {
        "metadata": {
            "title": "OWASP ISTG Cross-Framework Gap Analysis Report",
            "description": "Analysis of compliance coverage gaps across IEC 62443, NIST CSF 2.0, EU RED, and EU CRA/ETSI",
            "total_test_cases": len(test_cases),
            "frameworks_analyzed": ["IEC 62443", "NIST CSF 2.0", "EU RED", "EU CRA/ETSI"]
        }
    }
    
    print("Analyzing framework coverage...")
    coverage_analysis = analyze_framework_coverage(test_cases)
    report.update(coverage_analysis)
    
    print("Analyzing cross-framework overlaps...")
    overlaps = analyze_cross_framework_overlaps(test_cases)
    report["cross_framework_overlaps"] = overlaps
    
    print("Identifying coverage gaps...")
    gaps = identify_coverage_gaps(test_cases)
    report["coverage_gaps"] = gaps
    
    print("Generating recommendations...")
    recommendations = generate_recommendations(coverage_analysis, overlaps, gaps)
    report["recommendations"] = recommendations
    
    return report

def export_gap_analysis(report, output_file=GAP_ANALYSIS_JSON):
    """Export gap analysis report as JSON"""
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Gap analysis report exported to: {output_file}")

def print_gap_analysis_summary(report):
    """Print a summary of gap analysis results"""
    print("\n" + "="*70)
    print("OWASP ISTG CROSS-FRAMEWORK GAP ANALYSIS SUMMARY")
    print("="*70)
    
    metadata = report["metadata"]
    print(f"\nTotal Test Cases Analyzed: {metadata['total_test_cases']}")
    
    print("\nFramework Coverage Summary:")
    for framework, coverage in report["framework_coverage"].items():
        print(f"  {framework}:")
        print(f"    Coverage: {coverage['coverage_percentage']:.1f}% ({coverage['covered_test_cases']}/{coverage['applicable_test_cases']} applicable)")
        print(f"    TBD: {coverage['tbd_test_cases']} test cases")
        print(f"    Not Applicable: {coverage['not_applicable_test_cases']} test cases")
    
    overlaps = report["cross_framework_overlaps"]
    print(f"\nCross-Framework Analysis:")
    print(f"  Multi-framework test cases: {len(overlaps['multi_framework_tests'])}")
    print(f"  Universal test cases (all 4 frameworks): {len(overlaps['all_frameworks'])}")
    
    gaps = report["coverage_gaps"]
    print(f"\nCoverage Gaps:")
    print(f"  Completely unmapped tests: {len(gaps['unmapped_tests'])}")
    print(f"  Critical gaps (high-risk, poorly mapped): {len(gaps['critical_gaps'])}")
    
    # Framework-specific gaps
    for framework, framework_gaps in gaps["framework_specific_gaps"].items():
        if framework_gaps:
            print(f"  {framework} gaps: {len(framework_gaps)} test cases")
    
    print(f"\nTop Priority Actions:")
    for i, action in enumerate(report["recommendations"]["priority_actions"][:3], 1):
        print(f"  {i}. {action['action']}: {action['description']}")
    
    print(f"\nTop Critical Gaps:")
    for i, gap in enumerate(gaps["critical_gaps"][:5], 1):
        print(f"  {i}. {gap['id']} - {gap['title'][:50]}...")
        print(f"     Component: {gap['component']}, Mapped to {gap['mapped_frameworks']}/4 frameworks")
    
    if overlaps["all_frameworks"]:
        print(f"\nUniversal Test Cases (All Frameworks):")
        for i, test in enumerate(overlaps["all_frameworks"][:5], 1):
            print(f"  {i}. {test['id']} - {test['title'][:50]}...")

def main():
    """Main function to generate gap analysis report"""
    print("Loading compliance data...")
    data = load_data()
    
    if not data:
        return
    
    print("Generating gap analysis report...")
    report = generate_gap_analysis_report(data)
    
    print("Exporting gap analysis report...")
    export_gap_analysis(report)
    
    print_gap_analysis_summary(report)
    
    print(f"\nDetailed gap analysis available at: {GAP_ANALYSIS_JSON}")

if __name__ == "__main__":
    main()
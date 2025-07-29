#!/usr/bin/env python3

import json
from os import walk
from os.path import dirname, abspath, join

ROOT_DIR = dirname(dirname(abspath(__file__)))

CHECKLIST_DIR = join(ROOT_DIR, "checklists")
TEST_CASE_DIR = join(ROOT_DIR, "src", "03_test_cases")
TOOL_DIR = join(ROOT_DIR, "scripts")

COMPLIANCE_MAPPINGS_FILE = join(TOOL_DIR, "compliance_mappings.json")
CHECKLIST_JSON = join(CHECKLIST_DIR, "compliance_checklist.json")
CHECKLIST_MARKDOWN = join(CHECKLIST_DIR, "compliance_checklist.md")

MD_TABLE_HEADER = "|Test ID|Test Name|Status|Notes|IEC 62443|NIST CSF 2.0|EU RED|EU CRA/ETSI|\n|-|-|-|-|-|-|-|-|\n"
MD_STYLE_CATEGORY = "**"

def main():
    # step 1: parse test cases from markdown files
    test_case_catalog = parse_test_cases()
    
    # step 2: load compliance mappings
    compliance_mappings = load_compliance_mappings()
    
    # step 3: merge test cases with compliance data
    enhanced_catalog = merge_compliance_data(test_case_catalog, compliance_mappings)
    
    # step 4: export enhanced test cases
    export_test_cases_json(enhanced_catalog)
    export_test_cases_markdown_with_compliance(enhanced_catalog)

def parse_test_cases(test_case_dir=TEST_CASE_DIR):
    test_case_catalog = {}

    # walk through directory structure of testing guide
    for (dirpath, dirnames, filenames) in walk(test_case_dir):

        # skip root directory of the test case chapter (first iteration of the loop)
        if dirpath != test_case_dir:
            component_id = None

            # each subdirectory of the test case chapter resembles a component (i.e., component directory)
            # each component directory should have a "README.md" file which includes all test cases for the component
            if "README.md" in filenames:
                test_cases_component = parse_file(join(dirpath, "README.md"))
                test_case_catalog = test_case_catalog | test_cases_component

                if len(test_cases_component.keys()) > 0:
                    component_id = list(test_cases_component.keys())[0]

                # remove "README.md" from list of files to avoid parsing it two times
                filenames.remove("README.md")

            # only parse other files in the component directory if a component ID was set (meaning that the "README.md" file has been parsed successfully)
            if component_id is not None:

                # parse other files in the component directory
                # every file besides "README.md" resembles a component specialization
                for filename in filenames:

                    test_cases_component_specialization = parse_file(join(dirpath, filename))

                    if "specializations" not in test_case_catalog[component_id]:
                        test_case_catalog[component_id]["specializations"] = {}

                    test_case_catalog[component_id]["specializations"] = test_case_catalog[component_id]["specializations"] | test_cases_component_specialization

    return test_case_catalog

def parse_file(filepath):
    file = open(filepath, "r")
    content = {}

    # loop through each line in the file
    for line in file:

        # only parse headlines that have an ID
        if line[0] == "#" and "(" in line:

            # parse title
            title = line.split("# ")[1].split(" (")[0]

            # parse ID
            id = line.split("(")[1][0:-2]

            if line.count("#") == 1:
                # title of component or component specialization
                chapter = title.split(" ")[0]
                title = title.split(". ")[1]

                content = {
                    id: {
                        "chapter": chapter,
                        "title": title,
                        "categories": {}
                    }
                }

            elif line.count("#") == 2:
                # title of test case category
                component_id = "-".join(id.split("-")[0:-1])
                content[component_id]["categories"][id] = {
                    "title": title,
                    "test_cases": {}
                }

            elif line.count("#") == 3:
                # title of test case
                component_id = "-".join(id.split("-")[0:-2])
                category_id = "-".join(id.split("-")[0:-1])
                content[component_id]["categories"][category_id]["test_cases"][id] = {
                    "title": title
                }

    file.close()
    return content

def load_compliance_mappings():
    """Load compliance mappings from JSON file"""
    try:
        with open(COMPLIANCE_MAPPINGS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: Compliance mappings file not found at {COMPLIANCE_MAPPINGS_FILE}")
        return {"compliance_frameworks": {}, "test_case_mappings": {}}

def merge_compliance_data(test_case_catalog, compliance_mappings):
    """Merge test case catalog with compliance mapping data"""
    enhanced_catalog = test_case_catalog.copy()
    
    # Add compliance framework info to catalog
    enhanced_catalog["compliance_frameworks"] = compliance_mappings.get("compliance_frameworks", {})
    
    # Enhance each test case with compliance data
    for component_id in enhanced_catalog:
        if component_id == "compliance_frameworks":
            continue
            
        component = enhanced_catalog[component_id]
        
        # Process main component categories
        if "categories" in component:
            for category_id in component["categories"]:
                category = component["categories"][category_id]
                if "test_cases" in category:
                    for test_case_id in category["test_cases"]:
                        test_case = category["test_cases"][test_case_id]
                        
                        # Add compliance data if available
                        if test_case_id in compliance_mappings.get("test_case_mappings", {}):
                            compliance_data = compliance_mappings["test_case_mappings"][test_case_id]
                            test_case.update(compliance_data)
                        else:
                            # Add default compliance structure if no mapping exists
                            test_case["compliance_mappings"] = generate_default_compliance_mapping(test_case_id, category_id, component_id)
        
        # Process specializations
        if "specializations" in component:
            for spec_id in component["specializations"]:
                spec_component = component["specializations"][spec_id]
                if "categories" in spec_component:
                    for category_id in spec_component["categories"]:
                        category = spec_component["categories"][category_id]
                        if "test_cases" in category:
                            for test_case_id in category["test_cases"]:
                                test_case = category["test_cases"][test_case_id]
                                
                                # Add compliance data if available
                                if test_case_id in compliance_mappings.get("test_case_mappings", {}):
                                    compliance_data = compliance_mappings["test_case_mappings"][test_case_id]
                                    test_case.update(compliance_data)
                                else:
                                    # Add default compliance structure
                                    test_case["compliance_mappings"] = generate_default_compliance_mapping(test_case_id, category_id, spec_id)
    
    return enhanced_catalog

def generate_default_compliance_mapping(test_case_id, category_id, component_id):
    """Generate default compliance mapping structure for unmapped test cases"""
    return {
        "IEC_62443": {
            "applicable": True,
            "requirements": ["To be determined"],
            "security_level": "SL-1"
        },
        "NIST_CSF": {
            "functions": ["To be determined"],
            "categories": ["To be determined"],
            "iot_guidance": "To be determined"
        },
        "EU_RED": {
            "applicable": "TBD" if "WRLS" in component_id else False,
            "reason": "Wireless applicability to be determined" if "WRLS" in component_id else "Not wireless-specific"
        },
        "EU_CRA_ETSI": {
            "essential_requirements": ["To be determined"],
            "etsi_provisions": ["To be determined"]
        }
    }

def sort_ids_by_chapter(content):
    sorted_content = {}
    for id in content: 
        if id != "compliance_frameworks":
            sorted_content[content[id]["chapter"]] = id
    return dict(sorted(sorted_content.items())).values()

def export_test_cases_json(enhanced_catalog, output_file=CHECKLIST_JSON):
    """Export enhanced test case catalog as JSON"""
    with open(output_file, 'w') as f:
        json.dump(enhanced_catalog, f, indent=2)
    print(f"JSON checklist with compliance data exported to: {output_file}")

def export_test_cases_markdown_with_compliance(enhanced_catalog, output_file=CHECKLIST_MARKDOWN):
    """Export enhanced checklist as markdown with compliance columns"""
    
    output = "# Testing Checklist with Compliance Framework Mappings\n\n"
    output += "The following is the list of items to test during the assessment with mappings to major compliance frameworks:\n\n"
    output += "**Compliance Frameworks:**\n"
    
    # Add framework descriptions
    if "compliance_frameworks" in enhanced_catalog:
        frameworks = enhanced_catalog["compliance_frameworks"]
        for fw_key, fw_data in frameworks.items():
            output += f"- **{fw_data['name']}** ({fw_data['version']}): {fw_data['description']}\n"
    
    output += "\nNote: The `Status` column can be set for values similar to \"Pass\", \"Fail\", \"N/A\".\n\n"

    # loop through components
    for component_id in sort_ids_by_chapter(enhanced_catalog):
        component_title = enhanced_catalog[component_id]["title"]
        categories = enhanced_catalog[component_id]["categories"]

        output += f"\n## {component_title} ({component_id})\n" + MD_TABLE_HEADER

        # loop through categories
        for category_id in categories:
            test_cases = categories[category_id]["test_cases"]
            output += f"|{MD_STYLE_CATEGORY}{category_id}{MD_STYLE_CATEGORY}|{MD_STYLE_CATEGORY}{categories[category_id]['title']}{MD_STYLE_CATEGORY}|||||||||\n"

            # loop through test cases
            for test_case_id in test_cases:
                test_case = test_cases[test_case_id]
                
                # Extract compliance summary
                iec_summary = get_compliance_summary(test_case, 'IEC_62443')
                nist_summary = get_compliance_summary(test_case, 'NIST_CSF')
                red_summary = get_compliance_summary(test_case, 'EU_RED')
                cra_summary = get_compliance_summary(test_case, 'EU_CRA_ETSI')
                
                output += f"|{test_case_id}|{test_case['title']}|||{iec_summary}|{nist_summary}|{red_summary}|{cra_summary}|\n"

        # loop through component specializations
        if "specializations" in enhanced_catalog[component_id]:
            for specialization_id in sort_ids_by_chapter(enhanced_catalog[component_id]["specializations"]):
                specialization_title = enhanced_catalog[component_id]["specializations"][specialization_id]["title"]
                categories = enhanced_catalog[component_id]["specializations"][specialization_id]["categories"]
                output += f"\n### {specialization_title} ({specialization_id})\n" + MD_TABLE_HEADER

                # loop through categories
                for category_id in categories:
                    test_cases = categories[category_id]["test_cases"]
                    output += f"|{MD_STYLE_CATEGORY}{category_id}{MD_STYLE_CATEGORY}|{MD_STYLE_CATEGORY}{categories[category_id]['title']}{MD_STYLE_CATEGORY}|||||||||\n"

                    # loop through test cases
                    for test_case_id in test_cases:
                        test_case = test_cases[test_case_id]
                        
                        # Extract compliance summary
                        iec_summary = get_compliance_summary(test_case, 'IEC_62443')
                        nist_summary = get_compliance_summary(test_case, 'NIST_CSF')
                        red_summary = get_compliance_summary(test_case, 'EU_RED')
                        cra_summary = get_compliance_summary(test_case, 'EU_CRA_ETSI')
                        
                        output += f"|{test_case_id}|{test_case['title']}|||{iec_summary}|{nist_summary}|{red_summary}|{cra_summary}|\n"

    # write output to file
    with open(output_file, "w") as f:
        f.write(output)
    print(f"Markdown checklist with compliance data exported to: {output_file}")

def get_compliance_summary(test_case, framework_key):
    """Extract a short summary for compliance framework mapping"""
    if "compliance_mappings" not in test_case:
        return "N/A"
    
    mapping = test_case["compliance_mappings"].get(framework_key, {})
    
    if framework_key == "IEC_62443":
        if mapping.get("applicable", True):
            return mapping.get("security_level", "TBD")
        return "N/A"
    elif framework_key == "NIST_CSF":
        functions = mapping.get("functions", [])
        if isinstance(functions, list) and functions:
            return functions[0] if functions[0] != "To be determined" else "TBD"
        return "TBD"
    elif framework_key == "EU_RED":
        if mapping.get("applicable", False):
            articles = mapping.get("articles", [])
            if isinstance(articles, list) and articles:
                return articles[0]
            return "Yes"
        return "N/A"
    elif framework_key == "EU_CRA_ETSI":
        requirements = mapping.get("essential_requirements", [])
        if isinstance(requirements, list) and requirements:
            return "Yes" if requirements[0] != "To be determined" else "TBD"
        return "TBD"
    
    return "TBD"

if __name__ == "__main__":
    main()
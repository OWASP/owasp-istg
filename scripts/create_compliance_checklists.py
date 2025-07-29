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
DASHBOARD_HTML = join(CHECKLIST_DIR, "compliance_dashboard.html")

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
    export_self_contained_dashboard(enhanced_catalog)

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

def export_self_contained_dashboard(enhanced_catalog, output_file=DASHBOARD_HTML):
    """Export self-contained HTML dashboard with embedded JSON data"""
    
    # Convert the enhanced_catalog to JSON string for embedding
    json_data = json.dumps(enhanced_catalog, indent=2)
    
    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OWASP ISTG Compliance Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: #f5f5f5;
            color: #333;
        }}

        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }}

        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }}

        .header p {{
            font-size: 1.1rem;
            opacity: 0.9;
        }}

        .controls {{
            background: white;
            padding: 1.5rem;
            margin: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            align-items: center;
        }}

        .control-group {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}

        .control-group label {{
            font-weight: 600;
            font-size: 0.9rem;
            color: #555;
        }}

        select, input {{
            padding: 0.5rem;
            border: 2px solid #ddd;
            border-radius: 4px;
            font-size: 0.9rem;
        }}

        select:focus, input:focus {{
            outline: none;
            border-color: #667eea;
        }}

        .framework-buttons {{
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }}

        .framework-btn {{
            padding: 0.5rem 1rem;
            background: #f0f0f0;
            border: 2px solid #ddd;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.8rem;
            transition: all 0.3s;
        }}

        .framework-btn.active {{
            background: #667eea;
            color: white;
            border-color: #667eea;
        }}

        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 1rem;
        }}

        .stat-card {{
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }}

        .stat-number {{
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
        }}

        .stat-label {{
            font-size: 0.9rem;
            color: #666;
            margin-top: 0.5rem;
        }}

        .content {{
            margin: 1rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }}

        .test-case {{
            padding: 1rem;
            border-bottom: 1px solid #eee;
            display: none;
        }}

        .test-case.visible {{
            display: block;
        }}

        .test-case:last-child {{
            border-bottom: none;
        }}

        .test-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }}

        .test-id {{
            font-weight: bold;
            color: #667eea;
            font-size: 0.9rem;
        }}

        .test-title {{
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }}

        .test-component {{
            background: #f0f0f0;
            padding: 0.25rem 0.5rem;
            border-radius: 12px;
            font-size: 0.8rem;
            color: #666;
        }}

        .compliance-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }}

        .compliance-card {{
            border: 1px solid #ddd;
            border-radius: 6px;
            padding: 1rem;
            background: #fafafa;
        }}

        .compliance-title {{
            font-weight: bold;
            color: #333;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
        }}

        .compliance-detail {{
            font-size: 0.8rem;
            color: #666;
            margin: 0.25rem 0;
        }}

        .status-indicator {{
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 0.5rem;
        }}

        .status-yes {{ background: #28a745; }}
        .status-no {{ background: #dc3545; }}
        .status-tbd {{ background: #ffc107; }}
        .status-na {{ background: #6c757d; }}

        .loading {{
            text-align: center;
            padding: 2rem;
            color: #666;
        }}

        .no-results {{
            text-align: center;
            padding: 2rem;
            color: #666;
            display: none;
        }}

        .success-message {{
            background: #d4edda;
            color: #155724;
            padding: 1rem;
            margin: 1rem;
            border-radius: 8px;
            border: 1px solid #c3e6cb;
        }}

        @media (max-width: 768px) {{
            .controls {{
                flex-direction: column;
                align-items: stretch;
            }}
            
            .framework-buttons {{
                justify-content: center;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>OWASP ISTG Compliance Dashboard</h1>
        <p>Interactive compliance framework mapping for IoT Security Testing Guide</p>
    </div>

    <div class="success-message">
        ✅ Dashboard loaded successfully with embedded compliance data! No external files required.
    </div>

    <div class="controls">
        <div class="control-group">
            <label>Component Filter:</label>
            <select id="componentFilter">
                <option value="">All Components</option>
            </select>
        </div>

        <div class="control-group">
            <label>Search Tests:</label>
            <input type="text" id="searchFilter" placeholder="Search test cases...">
        </div>

        <div class="control-group">
            <label>Framework Filter:</label>
            <div class="framework-buttons">
                <button class="framework-btn active" data-framework="all">All Frameworks</button>
                <button class="framework-btn" data-framework="IEC_62443">IEC 62443</button>
                <button class="framework-btn" data-framework="NIST_CSF">NIST CSF 2.0</button>
                <button class="framework-btn" data-framework="EU_RED">EU RED</button>
                <button class="framework-btn" data-framework="EU_CRA_ETSI">EU CRA/ETSI</button>
            </div>
        </div>
    </div>

    <div class="stats">
        <div class="stat-card">
            <div class="stat-number" id="totalTests">0</div>
            <div class="stat-label">Total Test Cases</div>
        </div>
        <div class="stat-card">
            <div class="stat-number" id="mappedTests">0</div>
            <div class="stat-label">Mapped Test Cases</div>
        </div>
        <div class="stat-card">
            <div class="stat-number" id="frameworks">4</div>
            <div class="stat-label">Compliance Frameworks</div>
        </div>
        <div class="stat-card">
            <div class="stat-number" id="coverage">0%</div>
            <div class="stat-label">Coverage</div>
        </div>
    </div>

    <div class="content">
        <div class="loading" id="loading" style="display: none;">Loading compliance data...</div>
        <div class="no-results" id="noResults">No test cases match the current filters.</div>
        <div id="testCases"></div>
    </div>

    <script>
        // Embedded compliance data - no external file needed!
        const complianceData = {json_data};
        
        let allTestCases = [];
        let filteredTestCases = [];

        // Initialize dashboard with embedded data
        function initializeDashboard() {{
            try {{
                processData();
                setupFilters();
                updateStats();
                renderTestCases();
                console.log('Dashboard initialized successfully with embedded data');
            }} catch (error) {{
                console.error('Error initializing dashboard:', error);
                document.getElementById('testCases').innerHTML = 
                    '<div style="padding: 2rem; text-align: center; color: #dc3545;">Error initializing dashboard. Check console for details.</div>';
            }}
        }}

        // Process raw data into flat test case array
        function processData() {{
            allTestCases = [];
            
            for (const componentId in complianceData) {{
                if (componentId === 'compliance_frameworks') continue;
                
                const component = complianceData[componentId];
                
                // Process main categories
                if (component.categories) {{
                    for (const categoryId in component.categories) {{
                        const category = component.categories[categoryId];
                        if (category.test_cases) {{
                            for (const testId in category.test_cases) {{
                                const testCase = category.test_cases[testId];
                                allTestCases.push({{
                                    id: testId,
                                    title: testCase.title,
                                    component: component.title,
                                    componentId: componentId,
                                    category: category.title,
                                    categoryId: categoryId,
                                    compliance_mappings: testCase.compliance_mappings || {{}},
                                    risk_level: testCase.risk_level || 'Medium'
                                }});
                            }}
                        }}
                    }}
                }}
                
                // Process specializations
                if (component.specializations) {{
                    for (const specId in component.specializations) {{
                        const spec = component.specializations[specId];
                        if (spec.categories) {{
                            for (const categoryId in spec.categories) {{
                                const category = spec.categories[categoryId];
                                if (category.test_cases) {{
                                    for (const testId in category.test_cases) {{
                                        const testCase = category.test_cases[testId];
                                        allTestCases.push({{
                                            id: testId,
                                            title: testCase.title,
                                            component: spec.title,
                                            componentId: specId,
                                            category: category.title,
                                            categoryId: categoryId,
                                            compliance_mappings: testCase.compliance_mappings || {{}},
                                            risk_level: testCase.risk_level || 'Medium'
                                        }});
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }}
            
            filteredTestCases = [...allTestCases];
        }}

        // Setup filter controls
        function setupFilters() {{
            // Populate component filter
            const componentFilter = document.getElementById('componentFilter');
            const components = [...new Set(allTestCases.map(tc => tc.component))].sort();
            
            components.forEach(component => {{
                const option = document.createElement('option');
                option.value = component;
                option.textContent = component;
                componentFilter.appendChild(option);
            }});

            // Setup event listeners
            componentFilter.addEventListener('change', applyFilters);
            document.getElementById('searchFilter').addEventListener('input', applyFilters);
            
            document.querySelectorAll('.framework-btn').forEach(btn => {{
                btn.addEventListener('click', (e) => {{
                    document.querySelectorAll('.framework-btn').forEach(b => b.classList.remove('active'));
                    e.target.classList.add('active');
                    applyFilters();
                }});
            }});
        }}

        // Apply all filters
        function applyFilters() {{
            const componentFilter = document.getElementById('componentFilter').value;
            const searchFilter = document.getElementById('searchFilter').value.toLowerCase();
            const frameworkFilter = document.querySelector('.framework-btn.active').dataset.framework;

            filteredTestCases = allTestCases.filter(tc => {{
                // Component filter
                if (componentFilter && tc.component !== componentFilter) return false;
                
                // Search filter
                if (searchFilter && !tc.title.toLowerCase().includes(searchFilter) && 
                    !tc.id.toLowerCase().includes(searchFilter)) return false;
                
                // Framework filter
                if (frameworkFilter !== 'all') {{
                    const mapping = tc.compliance_mappings[frameworkFilter];
                    if (!mapping || (mapping.applicable === false)) return false;
                }}
                
                return true;
            }});

            updateStats();
            renderTestCases();
        }}

        // Update statistics
        function updateStats() {{
            document.getElementById('totalTests').textContent = allTestCases.length;
            document.getElementById('mappedTests').textContent = 
                allTestCases.filter(tc => Object.keys(tc.compliance_mappings).length > 0).length;
            
            const coverage = allTestCases.length > 0 ? 
                Math.round((allTestCases.filter(tc => Object.keys(tc.compliance_mappings).length > 0).length / allTestCases.length) * 100) : 0;
            document.getElementById('coverage').textContent = coverage + '%';
        }}

        // Render test cases
        function renderTestCases() {{
            const container = document.getElementById('testCases');
            const noResults = document.getElementById('noResults');
            
            if (filteredTestCases.length === 0) {{
                container.innerHTML = '';
                noResults.style.display = 'block';
                return;
            }}
            
            noResults.style.display = 'none';
            
            container.innerHTML = filteredTestCases.map(tc => `
                <div class="test-case visible">
                    <div class="test-header">
                        <div>
                            <div class="test-id">${{tc.id}}</div>
                            <div class="test-title">${{tc.title}}</div>
                        </div>
                        <div class="test-component">${{tc.component}}</div>
                    </div>
                    <div class="compliance-grid">
                        ${{renderComplianceCards(tc.compliance_mappings)}}
                    </div>
                </div>
            `).join('');
        }}

        // Render compliance cards for a test case
        function renderComplianceCards(mappings) {{
            const frameworks = [
                {{ key: 'IEC_62443', name: 'IEC 62443' }},
                {{ key: 'NIST_CSF', name: 'NIST CSF 2.0' }},
                {{ key: 'EU_RED', name: 'EU RED' }},
                {{ key: 'EU_CRA_ETSI', name: 'EU CRA/ETSI' }}
            ];

            return frameworks.map(fw => {{
                const mapping = mappings[fw.key] || {{}};
                return `
                    <div class="compliance-card">
                        <div class="compliance-title">
                            ${{getStatusIndicator(mapping)}} ${{fw.name}}
                        </div>
                        ${{renderComplianceDetails(fw.key, mapping)}}
                    </div>
                `;
            }}).join('');
        }}

        // Get status indicator
        function getStatusIndicator(mapping) {{
            if (!mapping || Object.keys(mapping).length === 0) {{
                return '<span class="status-indicator status-na"></span>';
            }}
            if (mapping.applicable === false) {{
                return '<span class="status-indicator status-na"></span>';
            }}
            if (mapping.applicable === true || mapping.applicable === undefined) {{
                const hasTBD = JSON.stringify(mapping).includes('To be determined') || 
                              JSON.stringify(mapping).includes('TBD');
                return hasTBD ? 
                    '<span class="status-indicator status-tbd"></span>' : 
                    '<span class="status-indicator status-yes"></span>';
            }}
            return '<span class="status-indicator status-tbd"></span>';
        }}

        // Render compliance details
        function renderComplianceDetails(frameworkKey, mapping) {{
            if (!mapping || Object.keys(mapping).length === 0) {{
                return '<div class="compliance-detail">No mapping available</div>';
            }}

            if (mapping.applicable === false) {{
                return `<div class="compliance-detail">Not applicable: ${{mapping.reason || 'N/A'}}</div>`;
            }}

            let details = [];

            switch (frameworkKey) {{
                case 'IEC_62443':
                    if (mapping.security_level) {{
                        details.push(`Security Level: ${{mapping.security_level}}`);
                    }}
                    if (mapping.foundational_requirement) {{
                        details.push(`FR: ${{mapping.foundational_requirement}}`);
                    }}
                    break;

                case 'NIST_CSF':
                    if (mapping.functions && Array.isArray(mapping.functions)) {{
                        details.push(`Functions: ${{mapping.functions.join(', ')}}`);
                    }}
                    if (mapping.categories && Array.isArray(mapping.categories)) {{
                        details.push(`Categories: ${{mapping.categories.slice(0, 2).join(', ')}}`);
                    }}
                    break;

                case 'EU_RED':
                    if (mapping.articles && Array.isArray(mapping.articles)) {{
                        details.push(`Articles: ${{mapping.articles.join(', ')}}`);
                    }}
                    if (mapping.requirements && Array.isArray(mapping.requirements)) {{
                        details.push(`Requirements: ${{mapping.requirements[0]}}`);
                    }}
                    break;

                case 'EU_CRA_ETSI':
                    if (mapping.essential_requirements && Array.isArray(mapping.essential_requirements)) {{
                        details.push(`Requirements: ${{mapping.essential_requirements.join(', ')}}`);
                    }}
                    if (mapping.etsi_provisions && Array.isArray(mapping.etsi_provisions)) {{
                        details.push(`ETSI: ${{mapping.etsi_provisions.slice(0, 1).join(', ')}}`);
                    }}
                    break;
            }}

            return details.length > 0 ? 
                details.map(d => `<div class="compliance-detail">${{d}}</div>`).join('') :
                '<div class="compliance-detail">Mapping available</div>';
        }}

        // Initialize the dashboard when page loads
        document.addEventListener('DOMContentLoaded', initializeDashboard);
    </script>
</body>
</html>'''

    # Write the self-contained HTML file
    with open(output_file, 'w') as f:
        f.write(html_template)
    
    print(f"Self-contained HTML dashboard exported to: {output_file}")

if __name__ == "__main__":
    main()
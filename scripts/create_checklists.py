#!/usr/bin/env python3.10

from os import walk
from os.path import dirname, abspath, join
from openpyxl import load_workbook


ROOT_DIR = dirname(dirname(abspath(__file__)))

CHECKLIST_DIR = join(ROOT_DIR, "checklists")
TEST_CASE_DIR = join(ROOT_DIR, "src", "03_test_cases")
TOOL_DIR = join(ROOT_DIR, "scripts")

CHECKLIST_MARKDOWN = join(CHECKLIST_DIR, "checklist.md")
CHECKLIST_TEMPLATE_MARKDOWN = join(TOOL_DIR, "checklist_template.md")

CHECKLIST_EXCEL = join(CHECKLIST_DIR, "checklist.xlsx")
CHECKLIST_TEMPLATE_EXCEL = join(TOOL_DIR, "checklist_template.xlsx")

MD_TABLE_HEADER = "|Test ID|Test Name|Status|Notes|\n|-|-|-|-|\n"
MD_STYLE_CATEGORY = "**"


def main():
    # step 1: parse test cases from markdown files
    test_case_catalog = parse_test_cases()

    # step 2: export test cases as checklists
    export_test_cases_markdown(test_case_catalog)
    export_test_cases_excel(test_case_catalog)


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

            match line.count("#"):
                # title of component or component specialization
                case 1:
                    chapter = title.split(" ")[0]
                    title = title.split(". ")[1]

                    content = {
                        id: {
                            "chapter": chapter,
                            "title": title,
                            "categories": {}
                        }
                    }

                # title of test case category
                case 2:
                    component_id = "-".join(id.split("-")[0:-1])
                    content[component_id]["categories"][id] = {
                        "title": title,
                        "test_cases": {}
                    }

                # title of test case
                case 3:
                    component_id = "-".join(id.split("-")[0:-2])
                    category_id = "-".join(id.split("-")[0:-1])
                    content[component_id]["categories"][category_id]["test_cases"][id] = {
                        "title": title
                    }

    file.close()
    return content


def sort_ids_by_chapter(content):
    sorted_content = {}
    for id in content: sorted_content[content[id]["chapter"]] = id
    return dict(sorted(sorted_content.items())).values()


def export_test_cases_markdown(test_case_catalog, checklist=CHECKLIST_MARKDOWN, checklist_template=CHECKLIST_TEMPLATE_MARKDOWN):
    # read content from template
    file_template = open(checklist_template, "r")
    content_template = file_template.read()
    file_template.close()

    # add template content to output
    output = content_template + "\n"

    # loop through components
    for component_id in sort_ids_by_chapter(test_case_catalog):
        component_title = test_case_catalog[component_id]["title"]
        categories = test_case_catalog[component_id]["categories"]

        output += "\n## " + component_title + " (" + component_id + ")" + "\n" + MD_TABLE_HEADER

        # loop through categories
        for category_id in categories:
            test_cases = categories[category_id]["test_cases"]
            output += "|" + "|".join([MD_STYLE_CATEGORY + category_id + MD_STYLE_CATEGORY, MD_STYLE_CATEGORY + categories[category_id]["title"] + MD_STYLE_CATEGORY, "", "", "\n"])

            # loop through test cases
            for test_case_id in test_cases:
                output += "|" + "|".join([test_case_id, test_cases[test_case_id]["title"], "", "", "\n"])

        # loop through component specializations
        if "specializations" in test_case_catalog[component_id]:
            for specialization_id in sort_ids_by_chapter(test_case_catalog[component_id]["specializations"]):
                specialization_title = test_case_catalog[component_id]["specializations"][specialization_id]["title"]
                categories = test_case_catalog[component_id]["specializations"][specialization_id]["categories"]
                output += "\n### " + specialization_title + " (" + specialization_id + ")" + "\n" + MD_TABLE_HEADER

                # loop through categories
                for category_id in categories:
                    test_cases = categories[category_id]["test_cases"]
                    output += "|" + "|".join([MD_STYLE_CATEGORY + category_id + MD_STYLE_CATEGORY,
                                              MD_STYLE_CATEGORY + categories[category_id]["title"] + MD_STYLE_CATEGORY,
                                              "", "", "\n"])

                    # loop through test cases
                    for test_case_id in test_cases:
                        output += "|" + "|".join([test_case_id, test_cases[test_case_id]["title"], "", "", "\n"])

    # write output to file
    file_checklist = open(checklist, "w")
    file_checklist.write(output)
    file_checklist.close()


def export_test_cases_excel(test_case_catalog, checklist=CHECKLIST_EXCEL, checklist_template=CHECKLIST_TEMPLATE_EXCEL):
    # read content from template
    excel_wb = load_workbook(checklist_template)
    excel_ws = excel_wb["Checklist"]

    row = 2

    # loop through components
    for component_id in sort_ids_by_chapter(test_case_catalog):
        categories = test_case_catalog[component_id]["categories"]

        # loop through categories
        for category_id in categories:
            test_cases = categories[category_id]["test_cases"]

            # loop through test cases
            for test_case_id in test_cases:
                excel_ws["A" + str(row)] = test_case_id
                excel_ws["B" + str(row)] = test_case_catalog[component_id]["title"]
                excel_ws["C" + str(row)] = categories[category_id]["title"]
                excel_ws["D" + str(row)] = test_cases[test_case_id]["title"]
                row += 1

        # loop through component specializations
        if "specializations" in test_case_catalog[component_id]:
            for specialization_id in sort_ids_by_chapter(test_case_catalog[component_id]["specializations"]):
                categories = test_case_catalog[component_id]["specializations"][specialization_id]["categories"]

                # loop through categories
                for category_id in categories:
                    test_cases = categories[category_id]["test_cases"]

                    # loop through test cases
                    for test_case_id in test_cases:
                        excel_ws["A" + str(row)] = test_case_id
                        excel_ws["B" + str(row)] = test_case_catalog[component_id]["specializations"][specialization_id]["title"]
                        excel_ws["C" + str(row)] = categories[category_id]["title"]
                        excel_ws["D" + str(row)] = test_cases[test_case_id]["title"]
                        row += 1

    # write output to file
    excel_wb.save(checklist)


main()

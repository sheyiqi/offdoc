import argparse
import os
import sys
import pandas
import math
import numpy
from pprint import pprint
from tabulate import tabulate


def parser():
    parse = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='A script to trans markdown file to SpreadT`s datasheet.',
        epilog="""
Example:
    sys.argv[0] -version
    sys.argv[0] -help
    sys.argv[0] -cfg xx.cfg -template template_001 -output xxx.md

                                                by sheyiqi
                                                2026/05/08

        """)
    
    parse.add_argument("-version", action="version", version="{} 1.0".format(sys.argv[0]))
    parse.add_argument("-cfg", help="specify a datasheet configuration file.", required=True)
    parse.add_argument("-template", help="specify a datasheet template dir.", required=True)
    parse.add_argument("-output", help="specify a output markdown file name.", required=True)
    args = parse.parse_args()
    print(args)
    cfg = args.cfg
    if os.path.exists(cfg):
        pass
    else:
        print("{} not exists.".format(cfg))
    template = args.template.replace('"', "")
    if os.path.exists(template):
        pass
    else:
        print("{} not exists.".format(template))
    output = args.output
    return cfg, template, output

def get_index_from_excel(excel_file):
    excel_file_data = pandas.DataFrame(pandas.read_excel(excel_file, sheet_name='Datasheet_Config'))
    excel_file_data['Chapter'] = excel_file_data['Chapter'].ffill()
    row_sum = excel_file_data.shape[0]
    conf_list = list()
    for i in range(row_sum):
        row_data = list(excel_file_data.loc[i])
        if type(row_data[1]) is float and bool(row_data[2]):
            conf_list.append(row_data[0])
        else:
            if bool(row_data[2]):
                if row_data[0] in conf_list:
                    pass
                else:
                    conf_list.append(row_data[0])
                conf_list.append(row_data[1])
            else:
                pass
    return conf_list

def replace_fullwidth_spaces(df: pandas.DataFrame) -> pandas.DataFrame:
    """将DataFrame中所有字符串类型列中的全角空格替换为半角空格"""
    for col in df.select_dtypes(include=['str']).columns:
        row_sum = df.shape[0]
        for i in range(row_sum):
            df.at[i, col] = str(df[col].loc[i]).replace('\u3000', ' ').replace('\xa0', ' ')
    return df

def get_param_from_excel(excel_file):
    excel_file_data = pandas.DataFrame(pandas.read_excel(excel_file, sheet_name='General_Settings'))
    #excel_file_data = replace_fullwidth_spaces(excel_file_data)
    row_sum = excel_file_data.shape[0]
    param_dict = dict()
    for i in range(row_sum):
        row_data = list(excel_file_data.loc[i])
        param_dict[row_data[0]] = row_data[1]
    return param_dict


def get_table_from_excel(excel_file):
    table_dict = dict()
    for sheet_name in (pandas.ExcelFile(excel_file).sheet_names):
        if sheet_name.startswith("Table"):
            excel_file_data = pandas.DataFrame(pandas.read_excel(excel_file, sheet_name=sheet_name, dtype=str))
            excel_file_data['Table Name'] = excel_file_data['Table Name'].ffill()
            md_table_name = list(excel_file_data['Table Name'])[0]
            excel_file_data = excel_file_data.drop('Table Name', axis=1)
            if "Standard PVT Corners" in md_table_name:
                md_table_cont = tabulate(excel_file_data, headers="keys", tablefmt="grid", showindex=False, maxcolwidths=(40,10,6,6,20,30), colalign=("left","left","left","left","left","left"))
            elif "Timing Mode Settings" in md_table_name or 'Repair Elements Mode' in md_table_name or 'Performance Shape Settings' in md_table_name or 'Bit Write Enable' in md_table_name or 'CEN-Gating' in md_table_name:
                md_table_cont = tabulate(excel_file_data, headers="keys", tablefmt="grid", showindex=False, maxcolwidths=(15,70), colalign=("left","left"))
            else:
                md_table_cont = tabulate(excel_file_data, headers="keys", tablefmt="grid", showindex=False, maxcolwidths=(15,15,70), colalign=("left","left","left",))
            table_dict[md_table_name] = md_table_cont + "\n\n" + md_table_name
    return table_dict


def get_configtable_from_excel(excel_file):
    table_dict = dict()
    for sheet_name in (pandas.ExcelFile(excel_file).sheet_names):
        if sheet_name.startswith("ConfigTable"):
            excel_file_data = pandas.DataFrame(pandas.read_excel(excel_file, sheet_name=sheet_name, dtype=str))
            excel_file_data['Table Name'] = excel_file_data['Table Name'].ffill()
            md_table_name = list(excel_file_data['Table Name'])[0]
            excel_file_data = excel_file_data.drop('Table Name', axis=1)
            excel_file_data = excel_file_data[excel_file_data['Config']=='True']
            excel_file_data = excel_file_data.drop('Config', axis=1)
            md_table_cont = tabulate(excel_file_data, headers="keys", tablefmt="grid", showindex=False, maxcolwidths=(15,20,70), colalign=("left","left","left",))
            table_dict[md_table_name] = md_table_cont + "\n\n" + md_table_name
    return table_dict


def get_text_from_excel(excel_file):
    text_dict = dict()
    for sheet_name in (pandas.ExcelFile(excel_file).sheet_names):
        if sheet_name.startswith("Text"):
            excel_file_data = pandas.DataFrame(pandas.read_excel(excel_file, sheet_name=sheet_name, dtype=str))
            excel_file_data['Text Name'] = excel_file_data['Text Name'].ffill()
            md_text_name = list(excel_file_data['Text Name'])[0]
            excel_file_data = excel_file_data.drop('Text Name', axis=1)
            row_sum = excel_file_data.shape[0]
            text_list = list()
            for i in range(row_sum):
                row_data = list(excel_file_data.loc[i])
                if row_data[1] is str(True):
                    if row_data[0] in text_list:
                        pass
                    else:
                        text_list.append(row_data[0])
                else:
                    pass
            text_dict[md_text_name] = "\n".join(text_list) + '\n'
    return text_dict


def update_md(output,  param_dict, table_dict, text_dict, configtable_dict):
    with open (output, "r", encoding="utf-8") as fr:
        lines = fr.read()
    for key, value in table_dict.items():
        lines = lines.replace("{}".format(str(key)), str(value))
    for key, value in configtable_dict.items():
        lines = lines.replace("{}".format(str(key)), str(value))
    for key, value in text_dict.items():
        lines = lines.replace("{}".format(str(key)), str(value))
    for key, value in param_dict.items():
        lines = lines.replace("[{}]".format(str(key)), str(value))
    #print("""Update md file with parameters from excel file.""")
    with open(output, "w", encoding="utf-8") as fw:
        fw.write(lines)


def search_md(output, conf_list, template_dir, Compiler_Name, IP_Prefix):
    public_files = os.listdir(os.path.join(template_dir, "Public"))
    for i in range(len(public_files)):
        public_files[i] = os.path.join(template_dir, "Public", public_files[i])
    ip_files = os.listdir(os.path.join(template_dir, "Public", IP_Prefix))
    for i in range(len(ip_files)):
        ip_files[i] = os.path.join(template_dir, "Public", IP_Prefix, ip_files[i])
    compiler_files = os.listdir(os.path.join(template_dir, Compiler_Name))
    for i in range(len(compiler_files)):
        compiler_files[i] = os.path.join(template_dir, Compiler_Name, compiler_files[i])
    files = public_files + ip_files + compiler_files
    active_md = list()
    for file in files:
        if not os.path.isdir(file) and str(file).endswith(".md"):
            active_md.append(file)
    print(active_md)
    matched_md = list()
    for conf in conf_list:
        match_tag = 0
        for md_name in active_md:
            if "{}.md".format(conf) in md_name:
                matched_md.append(md_name)
                match_tag =1
        if match_tag != 1:
            raise FileExistsError("{} can not search {} md file.".format(sys.argv[0], conf))
            sys.exit("-1")
    pprint(matched_md, width=1000)
    ### generate total md
    total_cont = str()
    for md in matched_md:
        with open (md, "r", encoding="utf-8") as fr:
            lines = fr.read()
        total_cont = total_cont + lines + "\n"
    
    with open(output, "w", encoding="utf-8") as fw:
        fw.write(total_cont)


def main():
    excel_file, template_dir, output = parser()
    conf_list = get_index_from_excel(excel_file)
    param_dict = get_param_from_excel(excel_file)
    Compiler_Name = param_dict.get("Compiler Name")
    Template_Version = param_dict.get("Template Version")
    IP_Prefix = param_dict.get("IP Prefix")
    template_dir = os.path.join(template_dir, Template_Version)
    md_dir = os.path.join(template_dir, "md")
    Public_Table_path = os.path.join(template_dir, "Table", "Public", "Common_Datasheet_Config.xlsx")
    IP_Table_path = os.path.join(template_dir, "Table", "Public", IP_Prefix, "Common_Datasheet_Config.xlsx")
    Memory_Table_path = os.path.join(template_dir, "Table", Compiler_Name, "Local_Datasheet_Config.xlsx")
    figure_dir = os.path.join(template_dir, "Figure")
    param_dict["Template Path"] = figure_dir
    public_table_dict = get_table_from_excel(Public_Table_path)
    ip_table_dict = get_table_from_excel(IP_Table_path)
    local_table_dict = get_table_from_excel(Memory_Table_path)
    global_table_dict = get_table_from_excel(excel_file)
    configtable_dict = get_configtable_from_excel(excel_file)
    text_dict = get_text_from_excel(excel_file)
    search_md(output, conf_list, md_dir, Compiler_Name, IP_Prefix)
    table_dict = public_table_dict
    table_dict.update(global_table_dict)
    table_dict.update(ip_table_dict)
    table_dict.update(local_table_dict)
    update_md(output, param_dict, table_dict, text_dict, configtable_dict)


if __name__ == "__main__":
    main()
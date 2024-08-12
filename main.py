#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   main.py
@Time    :   2024/08/11 23:33:59
@Author  :   Carlos Fuego
@Version :   1.0
@Contact :   huanyang2022@gmail.com
@License :   Copyright (c) 2024 Carlos Fuego
@Desc    :   None
'''
import argparse
import json
import os
from datetime import datetime
from render import render_json_to_html,render_json_to_markdown

def get_formatted_timestamp():
    # 获取当前时间
    now = datetime.now()
    # 格式化时间戳为字符串
    formatted_timestamp = now.strftime('%Y%m%d%H%M')
    return formatted_timestamp

def search_keywords_on_arxiv(keywords,max_results=500):
    import arxiv
    arxiv_client = arxiv.Client()
    all_data = []
    for keyword in keywords:
        search = arxiv.Search(query=keyword, max_results=max_results, sort_by=arxiv.SortCriterion.LastUpdatedDate)
        results = arxiv_client.results(search)
        data = []
        for res in results:
            data.append(res._raw)
        all_data.append({
            "keyword": keyword,
            "arxiv_results": data
        })
    return all_data

def search_command(args):
    keywords = args.keyword
    max_results = args.max_results
    all_data = search_keywords_on_arxiv(keywords,max_results)
    
    filename = get_formatted_timestamp()
    os.makedirs(args.output_dir,exist_ok=True)
    os.makedirs(os.path.join(args.output_dir,"json"),exist_ok=True)
    os.makedirs(os.path.join(args.output_dir,"md"),exist_ok=True)
    os.makedirs(os.path.join(args.output_dir,"html"),exist_ok=True)
    json_output_path=os.path.join(args.output_dir,f"json/{filename}.json")
    json.dump(all_data,open(json_output_path,"w"),indent=4,ensure_ascii=False)
    
    if args.markdown:
        md_output_path= os.path.join(args.output_dir,f"md/{filename}.md")
        render_json_to_markdown(json_output_path,md_output_path)
        if args.over_readme:
            md_output_path= os.path.join(args.output_dir,f"md/README.md")
            render_json_to_markdown(json_output_path,md_output_path)
    if args.html:
        html_output_path= os.path.join(args.output_dir,f"html/{filename}.html")
        if args.over_index:
            html_output_path= os.path.join(args.output_dir,f"index.html")
        render_json_to_html(json_output_path,html_output_path)
    
def render_command(args):
    input_path = args.input
    output_path = args.output
    
    if args.markdown:
        render_json_to_markdown(input_path,output_path)
    if args.html:
        render_json_to_html(input_path,output_path)

def main():
    parser = argparse.ArgumentParser(description="arxiv")
    subparsers = parser.add_subparsers(dest='command', help='')

    search_parser = subparsers.add_parser(name='search', help='')
    search_parser.add_argument('--keyword', type=str, action='append', help='',required=True)
    search_parser.add_argument('--max_results', type=int, default=500, help='')
    search_parser.add_argument('--output_dir', type=str, default='keyword/', help='')
    search_parser.add_argument('--markdown',action='store_true', help='',default=True)
    search_parser.add_argument('--html',action='store_true', help='',default=True)
    search_parser.add_argument('--over_index',action='store_true', help='',default=True)
    search_parser.add_argument('--over_readme',action='store_true', help='',default=True)

    
    render_parser = subparsers.add_parser(name='render', help='')
    render_parser.add_argument('--input', type=str, help='',required=True)
    render_parser.add_argument('--output', type=str, help='',required=True)
    render_parser.add_argument('--markdown',action='store_true', help='',default=True)
    render_parser.add_argument('--html',action='store_true', help='',default=False)
    
    args = parser.parse_args()
    if args.command=="search":
        search_command(args)
    elif args.command=="render":
        render_command(args)
    
    

if __name__ == "__main__":
    main()
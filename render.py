import json
from string import Template
def render_json_to_markdown(json_path,md_path):
    markdown_content = "# Arxiv Results\n"
    metadata_list = json.load(open(json_path,"r"))
    md_item_temlate = open("assets/md_item.template",'r').read()
    
    for data in metadata_list:
        keyword = data['keyword']
        paper_list = data['arxiv_results']
        template = Template(md_item_temlate)
        paper_md_data =""
        for idx,paper in enumerate(paper_list):
            title = paper['title'].replace('\n', ' ')
            authors = ', '.join([author['name'] for author in paper['authors']])
            summary = paper['summary'].replace('\n', ' ')
            updated = paper['updated']
            tags = ''.join([f"{tag['term']} " for tag in paper['tags']])
            arxiv_link = paper['link']
            pdf_link = arxiv_link.replace('abs/', 'pdf/')
            
            md_data = template.substitute(
                title=title, 
                authors=authors,
                updated_date=updated,
                summary=summary,
                arxiv_url=arxiv_link,
                pdf_url=pdf_link,
                tags=tags)
            paper_md_data+=md_data
        markdown_content+=f"## Keyword: {keyword} \n {paper_md_data}"
    open(md_path,"w").write(markdown_content)        

    

def render_json_to_html(json_path,html_path):
    metadata_list = json.load(open(json_path,"r"))
    # Start the HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ArXiv Results</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                width: 21cm;
                height: 29.7cm;
                padding: 2cm;
                box-sizing: border-box;
            }
            h1, h2 {
                color: #333;
            }
            .paper {
                border: 1px solid #ccc;
                padding: 1em;
                margin-bottom: 1em;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .authors, .summary, .updated, .tags, .links {
                margin: 0.5em 0;
            }
            .tags span {
                background-color: #f0f0f0;
                border-radius: 4px;
                padding: 0.2em 0.5em;
                margin-right: 0.5em;
            }
            .links a {
                margin-right: 1em;
                text-decoration: none;
                color: #1a73e8;
            }
            .links a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
    """
    for data in metadata_list:
        
        # Add the keyword as the main title
        html_content += f"<h1>Keyword: {data['keyword']}</h1>\n"
        
        # Iterate over each paper and add its details
        for idx, paper in enumerate(data['arxiv_results']):
            title = paper['title']
            authors = ', '.join([author['name'] for author in paper['authors']])
            summary = paper['summary'].replace('\n', ' ')
            updated = paper['updated']
            tags = ''.join([f"<span>{tag['term']}</span>" for tag in paper['tags']])
            links = ''.join([f"<a href='{link['href']}' target='_blank'>{link['title'] if 'title' in link else 'HTML'}</a>" for link in paper['links']])
            
            html_content += f"""
            <div class="paper">
                <h2>#{idx} {title}</h2>
                <div class="authors">
                    <strong>Authors:</strong> {authors}
                </div>
                <div class="summary">
                    <strong>Summary:</strong> {summary}
                </div>
                <div class="updated">
                    <strong>Updated:</strong> {updated}
                </div>
                <div class="tags">
                    <strong>Tags:</strong> {tags}
                </div>
                <div class="links">
                    {links}
                </div>
            </div>
            """
    
    # Close the HTML content
    html_content += """
    </body>
    </html>
    """
    open(html_path,"w").write(html_content)
import bs4


class GraphqlPageModifier:

    def __init__(self):
        pass

    def remove_script_and_style(self, page):
        for script in page.head.select("script"):
            script.extract()
        for link in page.head.select("link"):
            link.extract()

    def add_script(self, page):
        with open("public/javascripts/spectaql.min.js") as inf:
            script_txt = inf.read()
            script_tag = page.new_tag("script")
            script_tag.append(script_txt)
            page.head.append(script_tag)

    def add_style(self, page):
        with open("public/stylesheets/spectaql.min.css") as inf:
            style_txt = inf.read()
            style_tag = page.new_tag("style")
            style_tag.append(style_txt)
            page.head.append(style_tag)

    def modify(self):
        with open("public/index.html") as inf:
            page_txt = inf.read()
            page = bs4.BeautifulSoup(page_txt, "html.parser")
            self.remove_script_and_style(page)
            self.add_script(page)
            self.add_style(page)
            prettyHTML = page.prettify()
        with open("public/index.html", "w") as outf:
            outf.write(str(prettyHTML))


if __name__ == '__main__':
    publish_api_specs = GraphqlPageModifier()
    publish_api_specs.modify()

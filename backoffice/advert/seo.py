from rollyourown import seo

class BasicMetadata(seo.Metadata):
        title          = seo.Tag(max_length=68, head=True)
        keywords       = seo.KeywordTag()
        description    = seo.MetaTag(max_length=155)
        heading        = seo.Tag(name="h1")
        subheading     = seo.Tag(name="h2")
        extra          = seo.Raw(head=True)
        # Adding some fields for facebook (opengraph)
        og_title       = seo.MetaTag(name="og:title", populate_from="title", verbose_name="facebook title")
        og_description = seo.MetaTag(name="og:description", populate_from="description", verbose_name='facebook description')

	class Meta:
    	    use_sites = True
    	    use_cache = True    
    	    use_i18n = True
    	    groups = {'optional': ('heading',)}
    	    seo_models = ('advert', 'flatpages.FlatPage')
    	    seo_views = ('advert', )
    	    backends = ('path', 'model', 'view')
    	    verbose_name = "My basic example"
    	    verbose_name_plural = "My basic examples"

class MyMetadata(seo.Metadata):
    title       = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=155)
    keywords    = seo.KeywordTag()
    heading     = seo.Tag(name="h1")


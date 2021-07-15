document_format = '''<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>{screen_name}</title>
  <link>{user_link}</link>
  <description>{screen_name}'s twitter feed</description>
  {items}
</channel>

</rss>'''

text_only_item_format = '''<item>
    <title>{tweet_text}</title>
    <link>{tweet_link}</link>
</item>'''

# media_item_format = '''<item>
#     <title>{tweet_text}</title>
#     <link>{tweet_link}</link>
# </item>'''

media_item_format = '''<item>
    <title>{tweet_text}</title>
    <link>{tweet_link}</link>
    <enclosure url="{image_url}" length="200000" type="image/jpeg" />
</item>'''

# media_item_format = '''<item>
#     <title>{tweet_text}</title>
#     <link>{tweet_link}</link>
#     <![CDATA[
#         <img src="{image_url}"/>
#     ]]> 
# </item>'''


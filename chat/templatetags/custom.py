from django import template
from django.utils.safestring import mark_safe

register=template.Library()

def generate_review_html(sub_review_dic,magin_left):
    html=""
    for k,v in sub_review_dic.items():
        html += "<div style='margin-left:%spx' class='review-node'>"%magin_left+k.review-content+"</div>"
        if v:
            html += generate_review_html(v,magin_left+15)
    return html

def tree_search(review_dic,review_obj):
    for k,v in review_dic.items():
        if k==review_obj.parent_review:
            review_dic[k][review_obj]={}
            return
        else:
            tree_search(review_dic[k],review_obj)

@register.simple_tag
def build_review_tree(review_list):
    review_dic={}
    for review_obj in review_list:
        if review_obj.parent_review is None:
            review_dic[review_obj]={}
        else:
            tree_search(review_dic,review_obj)

    html="<div.class='review-bos'>"
    magin_left=0
    for k,v in review_dic.items():
        html += "<div class='review-node'>"+k.review-content+"</div>"
        html += generate_review_html(v,magin_left+15)
    html+="</div>"
    return mark_safe(html)

from lxml import etree
from manage_classes import ArticleData
from sklearn.feature_extraction.text import TfidfVectorizer

if __name__ == '__main__':
    # Global variables
    article_path = "news.xml"
    vectorizer = TfidfVectorizer()

    with open(article_path, 'r') as f:
        tree = etree.parse(f)
    root = tree.getroot()
    corpus = root[0]

    articles_obj = [article for article in corpus]
    article_data_list = [ArticleData(article[0].text, article[1].text) for article in articles_obj]
    dataset = [" ".join(article.converted_tokens) for article in article_data_list]

    tfidf_matrix = vectorizer.fit_transform(dataset)
    terms = vectorizer.get_feature_names_out()

    for i in range(len(article_data_list)):
        article_data_list[i].tfidf_calculations = tfidf_matrix[i]
        article_data_list[i].calc_most_common_words(terms)

    for article in article_data_list:
        print(str(article) + "\n")

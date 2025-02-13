
class Document:
    def __init__(self, document: str):
        self.document = document

def doc_search(query, top_k, libs, kb_ids, kb_file_ids):
    """
    实现检索逻辑，返回List[Document]
    return: List[Document]
    """
    
    doc=Document(document="""预防糖尿病一般需要注意控制体重、注意养成良好的生活习惯、进行适度的体育锻炼、控制压力、避免过度饮酒和吸烟；饮食上要注意清淡饮食、注意选择低糖饮食、增加蔬果摄入、选择健康蛋白质、增加膳食纤维摄入。具体分析如下：

一、生活上注意事项

1.注意控制体重：糖尿病是一种代谢性疾病，主要表现为血糖升高。体重超重或肥胖是糖尿病发生的危险因素之一，因此需要通过适当锻炼、健康的饮食来控制体重。

2.注意养成良好的生活习惯：日常生活中要保持规律的生活方式，避免过度疲劳，保持心情愉悦，有利于预防糖尿病。

3.进行适度的体育锻炼：定期进行适度的有氧运动，如快走、跑步、游泳等，可以帮助提高身体的胰岛素敏感性，降低糖尿病的风险。

""")
    return [doc]*10


def extract_docs(docs: list[Document]):

    doc_strs = [doc.document for doc in docs]
    return doc_strs

def doc_search_main(query, top_k, libs, kb_ids, kb_file_ids):

    docs = doc_search(query, top_k, libs, kb_ids, kb_file_ids)
    doc_strs = extract_docs(docs)
    return doc_strs

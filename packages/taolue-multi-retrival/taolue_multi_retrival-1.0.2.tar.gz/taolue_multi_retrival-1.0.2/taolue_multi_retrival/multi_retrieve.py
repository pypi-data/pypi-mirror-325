from taolue_multi_retrival.find_max_info import find_complete_info_texts
from taolue_multi_retrival.util import invoke_labeler_main, invoke_filter_main,process_next_query_info,remove_duplicate_substrings,check_query,search_rerank_func_wrap
from taolue_multi_retrival.conf import MAX_ITER, CONTINUE_TAG, FINISH_TAG
import traceback
from loguru import logger


def efficient_rag(search_rerank_func, query, top_k=10, libs=["es_chunk","es_summary","es_embedding","es_summary_embedding"], kb_ids=None, kb_file_ids=None):
    query=check_query(query)
    do_search_main=search_rerank_func_wrap(search_rerank_func)
    if not query: return []
    sample_chunks = {}
    iter = 0
    filter_input = ""
    while iter < MAX_ITER:
        try:
            #记录改写前的query
            query_filter_before=query
            next_query_info = []
            if iter == 0:
                chunks = do_search_main(query, libs, kb_ids, kb_file_ids, top_k)
            else: 
                #改写问题避免查询摘要库
                chunks = do_search_main(query=query, libs=["es_chunk","es_embedding"], kb_ids=kb_ids, kb_file_ids=kb_file_ids, top_k=top_k)
            infos, labels = invoke_labeler_main(query, chunks)
            sample_chunks[iter] = {
                "query": query,
                "filter_input": filter_input,
                "docs": [],
            }
            for chunk_info, label, chunk in zip(infos, labels, chunks):
                sample_chunk = {
                    "text": chunk,
                    "label": label,
                    "info": chunk_info,
                }
                sample_chunks[iter]["docs"].append(sample_chunk)

                if label == CONTINUE_TAG and chunk_info :
                    next_query_info.append(chunk_info)
            #只要有1个FINISH，则停止
            if len(next_query_info) == 0 or FINISH_TAG in labels:
                break
            #next_query_info去重
            next_query_info_=list(set(next_query_info))
            next_query_info_ = process_next_query_info(next_query_info_)
            next_query_info=find_complete_info_texts(next_query_info_)

            #query改写
            filter_input, filtered_query = invoke_filter_main(query, infos)
            query=remove_duplicate_substrings(filtered_query)

            #改写前后一致，则停止
            if query.strip()==query_filter_before.strip():
                break
            iter += 1
        except Exception as e:
            logger.error(f"第{iter}轮检索失败，原因：{e}{traceback.format_exc()}")
            break
    retrieve_texts=[doc["text"] for doc in sample_chunks[iter]["docs"] for iter in sample_chunks.keys()] if sample_chunks else []
    return retrieve_texts


    return 
if __name__ == "__main__":
    import time
    start=time.time()
    query = "如何预防糖尿病"
    sample_chunks = efficient_rag(query)
    import json
    print(json.dumps(sample_chunks, ensure_ascii=False, indent=4))
    print("time:",time.time()-start)

from typing import List

from category import Category
from document import Document
from topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        cur_category = [c for c in self.categories if c.id == category_id][0]
        cur_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        cur_topic = [c for c in self.topics if c.id == topic_id][0]
        cur_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        cur_doc = [d for d in self.documents if d.id == document_id][0]
        cur_doc.edit(new_file_name)

    def delete_category(self,category_id):
        cur_cat = [ c for c in self.categories if c.id == category_id][0]
        self.categories.remove(cur_cat)

    def delete_topic(self,topic_id):
        cur_top = [top for top in self.topics if top.id ==topic_id][0]
        self.topics.remove(cur_top)


    def delete_document(self,document_id):
        cur_doc = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(cur_doc)

    def get_document(self,document_id):
        cur_doc = [d for d in self.documents if d.id == document_id][0]
        return cur_doc

    # def __repr__(self):
        # res = ""
        # for d in self.documents:
        #     res += f"{d}\n"
        # return res
    def __repr__(self):
        return '\n'.join(map(str, self.documents))

from info import documents, directories


class ArchiveOfDocuments:

	def get_search_name_on_doc(self, doc_num):
		for doc in documents:
			if doc_num in doc['number']:
				person_name = doc['name']
				return person_name
		else:
			return 'Номер документ {doc_num} не найден'

	def get_search_shelf_on_doc(self, doc_num):
		for key, shelf in directories.items():
			if doc_num in directories[key]:
				num_shelf = key
				return num_shelf
		else:
			return f'Номер документ {doc_num} не найден'

	def get_list_of_doc(self):
		for dct in documents:
			print(f"№: {dct['number']}, тип: {dct['type']}, владелец: {dct['name']}")

	def get_add_doc(self, num_key, num_doc, **kwargs):
		if num_key in directories.keys():
			directories[num_key].append(num_doc)
			documents.append(kwargs)
			return 'Successfully!', True
		else:
			return f'Полка {num_key} отсутствует', False

	def get_del_doc(self, doc_num):
		for num, doc in enumerate(documents):
			if doc['number'] == doc_num:
				del documents[num]
				break
		for key, shelf in directories.items():
			if doc_num in directories[key]:
				del directories[key][shelf.index(doc_num)]
				return f'{doc_num} remove', True
		else:
			return f'Номер документа {doc_num} не найден', False

	def get_add_shelf(self, num_shelf):
		if num_shelf not in directories.keys():
			directories[num_shelf] = []
			return num_shelf, True
		return num_shelf, False

	def get_move_direct(self):
		doc_num = input('Введите номер документа: ')
		num_shelf_move = input('Введите номер полки: ')
		if type(directories.get(num_shelf_move)) == list:
			for key, shelf in directories.items():
				if doc_num in directories[key]:
					item = directories[key][shelf.index(doc_num)]
					directories[num_shelf_move].append(item)
					del directories[key][shelf.index(doc_num)]
					break
			else:
				return f'Номер документа {doc_num} не найден'
		else:
			return f'Полка {num_shelf_move} отсутствует'

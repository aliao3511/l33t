def mergeKLists(lists):
        dummy = ListNode(0)
        head = dummy
        processing = {i for i in range(0, len(lists))}
        while bool(processing):
            min_list = None
            for idx, pointer in enumerate(lists):
                if idx in processing: 
                    if pointer:
                        if min_list is None:
                            min_list = idx
                        else:
                            if pointer.val < lists[min_list].val:
                                min_list = idx
                    else:
                        processing.remove(idx)
            if min_list is not None:
                head.next = lists[min_list]
                lists[min_list] = lists[min_list].next
                head = head.next
        return dummy.next

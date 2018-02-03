(defun insert (item list1)

	(if (null list1)
		(list item)
		(if (< item (car list1))

			(cons item list1)
			(cons (car list1) (insert item (cdr list1))))))

(defun insertion_sort (list1)

	(if (null list1)
		list1
		(insert (car list1) (insertion_sort (cdr list1)))))

(print (insertion_sort '(9 8 7 6 5 4 3 2 1)))
(defun insert (item list1)

	(if (null list1)
		(list item)
		(if (<= (length item) (length (car list1)))

			(cons item list1)
			(cons (car list1) (insert item (cdr list1))))))

(defun lsort (list1)

	(if (null list1)
		list1
		(insert (car list1) (lsort (cdr list1)))))

(print (lsort '((A B C) (D E) (F G H) (D E) (I J K L) (M N) (O))))
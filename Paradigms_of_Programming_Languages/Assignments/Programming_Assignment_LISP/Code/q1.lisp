;Question 1

(defun subst (char1 char2 list1)
		(if (null list1) () 		;If the list is null, return nothing
			(if (atom (car list1)) 	;If the first element is an atom
				(if (equal (car list1) char1) 	;If the atom is equal to the character to be substituted
					(cons char2 (subst char1 char2 (cdr list1))) 	;Substitute the atom
					(cons (car list1) (subst char1 char2 (cdr list1)))) ; Dont substitute, as it is not equal
				(cons (subst char1 char2 (car list1)) (subst char1 char2 (cdr list1)))))) 	;Call subst on both the lists

; (print (subst 'a 'b '(a (a b c) (a d))))

;Question 2
(defun insert (item list1)

	(if (null list1)
		(list item) 	;If the list is null, return it
		(if (<= (length item) (length (car list1))) 	;If the length of the list is lesser than the first list, append

			(cons item list1)
			(cons (car list1) (insert item (cdr list1)))))) 	;Else recursively call the function

(defun lsort (list1)

	(if (null list1)
		list1
		(insert (car list1) (lsort (cdr list1))))) 				; Call the insertion sort function

(print (lsort '((A B C) (D E) (F G H) (D E) (I J K L) (M N) (O))))
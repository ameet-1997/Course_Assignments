;Question 1

(defun subst (char1 char2 list1)
		(if (null list1) () 		;If the list is null, return nothing
			(if (atom (car list1)) 	;If the first element is an atom
				(if (equal (car list1) char1) 	;If the atom is equal to the character to be substituted
					(cons char2 (subst char1 char2 (cdr list1))) 	;Substitute the atom
					(cons (car list1) (subst char1 char2 (cdr list1)))) ; Dont substitute, as it is not equal
				(cons (subst char1 char2 (car list1)) (subst char1 char2 (cdr list1)))))) 	;Call subst on both the lists

(print (subst 'a 'b '(a (a b c) (a d))))

;Question 2
(defun insert2 (item list1)

	(if (null list1)
		(list item) 	;If the list is null, return it
		(if (<= (length item) (length (car list1))) 	;If the length of the list is lesser than the first list, append

			(cons item list1)
			(cons (car list1) (insert2 item (cdr list1)))))) 	;Else recursively call the function

(defun lsort (list1)

	(if (null list1)
		list1
		(insert2 (car list1) (lsort (cdr list1))))) 				; Call the insertion sort function

(print (lsort '((A B C) (D E) (F G H) (D E) (I J K L) (M N) (O))))

;Question 3
;The code is the same as the previous program
(defun insert (item list1)

	(if (null list1) 	;If the list is null, return the list
		(list item)
		(if (< item (car list1)) 	;If the item is lesser than the first element, then add it to the starting of the list

			(cons item list1)
			(cons (car list1) (insert item (cdr list1)))))) 	;Else recursively call the function on (cdr list1)

(defun insertion_sort (list1)

	(if (null list1)
		list1
		(insert (car list1) (insertion_sort (cdr list1))))) 	;Make a call to the insertion sort

(print (insertion_sort '(9 8 7 6 5 4 3 2 1)))

;Question 4
(defun trans (list1)
	(apply #'mapcar #'list list1)) 		; Take the corresponsing elements of all the lists, and create 1 list with those as elements
										; mapcar command will automatically append all of them into one list
(print (trans '((a b c) (a b c) (a b c))))

;Question 5
(defun memoized (f)
	(let ((table (make-hash-table :test #'equal))) ; Arguments could be lists and not just atoms, hence use equal
												   ; Create a HashTable that stores all the arguments
		#'(lambda (&rest args)
	(multiple-value-bind (retrieved flag) (gethash args table) 	; gethash returns two values, store them using multiple-value-bind
	(if flag 						; If the value already exists in the HashTable, then just retrieve it
		retrieved
	(setf (gethash args table) 		; Else compute the value and store it in the HashTable
	(apply f args)))))))

; (setf (fdefinition 'funcname) (memoized #'funcname)) 	;This is to make sure when recursive functions are called, the symbol table entry is changed to the memoized function. Else the non-memoized function will get called.


;Question 6
(defun fib (n acc1 acc2) 	; First accumulator is the Fib(k) and the second is Fib(k+1)
(if (eql n 0) acc1 (fib (- n 1) acc2 (+ acc1 acc2)))) 	; If n is 0, return the accumulator
														; Else change the accumulator by doing fib(k) = fib(k-1)+fib(k-2)

(print (fib 8 0 1))
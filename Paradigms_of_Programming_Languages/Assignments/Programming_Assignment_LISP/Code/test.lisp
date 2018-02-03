(defun subst1 (char1 char2 list1)

	;Body

		(if (null list1) ();Do nothing if true
		
		(if (atom (car list1));else statement

			(if (equal (car list1) char1)

				(return-from subst1 (cons char2 (subst1 char1 char2 (cdr list1))))

				(return-from subst1 (cons (car list1) (subst1 char1 char2 (cdr list1))));else statement
			)

			;else statement
				(return-from subst1 (append (subst1 char1 char2 (car list1)) (subst1 char1 char2 (cdr list1))  ))
			

		)

		)


)

; ( print-elements-of-list (subst1 'a 'b '()    )    )
(subst1 'a 'b '(a (abc) (a d)))

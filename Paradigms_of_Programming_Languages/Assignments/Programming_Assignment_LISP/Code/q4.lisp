(defun trans (list1)
	(apply #'mapcar #'list list1))

(print (trans '((a b c) (a b c) (a b c))))
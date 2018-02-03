(defun memoized (f)
	(let ((table (make-hash-table :test #'equal))) ; Arguments could be lists and not just atoms
		#'(lambda (&rest args)
	(multiple-value-bind (retrieved flag) (gethash args table)
	(if flag
		retrieved
	(setf (gethash args table)
	(apply f args)))))))

; (setf (fdefinition 'funcname) (memoized #'funcname))
(defun fib (n acc1 acc2)
(if (eql n 0) acc1 (fib (- n 1) acc2 (+ acc1 acc2))))

(print (fib 8 0 1))
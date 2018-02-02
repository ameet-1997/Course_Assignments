.text
.globl    main
main:
move $fp, $sp
subu $sp, $sp, 88
sw $ra, -4($fp)
li $t0 8
move $a0 $t0
jal _halloc
move $t1 $v0
move $t2 $t1
li $t3 4
move $a0 $t3
jal _halloc
move $t4 $v0
move $t5 $t4
la $t6 MT4_Change
sw $t6, 4($t2)
la $t7 MT4_Start
sw $t7, 0($t2)
sw $t2, 0($t5)
move $t8 $t5
lw $t9, 0($t8)
lw $s0, 0($t9)
li $s1 1
li $s2 2
li $s3 3
li $s4 4
li $s5 5
li $s6 6
sw $t0, 12($sp)
sw $t1, 16($sp)
sw $t2, 20($sp)
sw $t3, 24($sp)
sw $t4, 28($sp)
sw $t5, 32($sp)
sw $t6, 36($sp)
sw $t7, 40($sp)
sw $t8, 44($sp)
sw $t9, 48($sp)
move $a0 $t8
move $a1 $s1
move $a2 $s2
move $a3 $s3
sw $s4, 0($sp)
sw $s5, 4($sp)
sw $s6, 8($sp)
jalr $s0
lw $t0, 12($sp)
lw $t1, 16($sp)
lw $t2, 20($sp)
lw $t3, 24($sp)
lw $t4, 28($sp)
lw $t5, 32($sp)
lw $t6, 36($sp)
lw $t7, 40($sp)
lw $t8, 44($sp)
lw $t9, 48($sp)
move $s7 $v0
move $a0 $s7
jal _print
lw $ra, -4($fp)
addu $sp, $sp, 88
j $ra

.text
.globl    MT4_Start
MT4_Start:
sw $fp, -8($sp)
move $fp, $sp
subu $sp, $sp, 104
sw $ra, -4($fp)
sw $s0, 12($sp)
sw $s1, 16($sp)
sw $s2, 20($sp)
sw $s3, 24($sp)
sw $s4, 28($sp)
sw $s5, 32($sp)
sw $s6, 36($sp)
sw $s7, 40($sp)
move $t0 $a0
move $t1 $a1
move $t2 $a2
move $t3 $a3
move $a0 $t1
jal _print
move $a0 $t2
jal _print
move $a0 $t3
jal _print
lw $v1, 0($fp)
move $a0 $v1
jal _print
lw $v1, 4($fp)
move $a0 $v1
jal _print
lw $v1, 8($fp)
move $a0 $v1
jal _print
move $t4 $t0
lw $t5, 0($t4)
lw $t6, 4($t5)
sw $t0, 44($sp)
sw $t1, 48($sp)
sw $t2, 52($sp)
sw $t3, 56($sp)
sw $t4, 60($sp)
sw $t5, 64($sp)
sw $t6, 68($sp)
sw $t7, 72($sp)
sw $t8, 76($sp)
sw $t9, 80($sp)
move $a0 $t4
lw $v1, 8($fp)
move $a1 $v1
lw $v1, 4($fp)
move $a2 $v1
lw $v1, 0($fp)
move $a3 $v1
sw $t3, 0($sp)
sw $t2, 4($sp)
sw $t1, 8($sp)
jalr $t6
lw $t0, 44($sp)
lw $t1, 48($sp)
lw $t2, 52($sp)
lw $t3, 56($sp)
lw $t4, 60($sp)
lw $t5, 64($sp)
lw $t6, 68($sp)
lw $t7, 72($sp)
lw $t8, 76($sp)
lw $t9, 80($sp)
move $v1 $v0
sw $v1, 8($fp)
lw $v0, 4($fp)
lw $v1, 8($fp)
add $v1, $v0, $v1
sw $v1, 4($fp)
lw $v1, 8($fp)
move $t7 $v1
move $v0 $t7
lw $s0, 12($sp)
lw $s1, 16($sp)
lw $s2, 20($sp)
lw $s3, 24($sp)
lw $s4, 28($sp)
lw $s5, 32($sp)
lw $s6, 36($sp)
lw $s7, 40($sp)
lw $ra, -4($fp)
lw $fp, 96($sp)
addu $sp, $sp, 104
j $ra

.text
.globl    MT4_Change
MT4_Change:
sw $fp, -8($sp)
move $fp, $sp
subu $sp, $sp, 104
sw $ra, -4($fp)
sw $s0, 12($sp)
sw $s1, 16($sp)
sw $s2, 20($sp)
sw $s3, 24($sp)
sw $s4, 28($sp)
sw $s5, 32($sp)
sw $s6, 36($sp)
sw $s7, 40($sp)
move $t0 $a1
move $t1 $a2
move $t2 $a3
move $a0 $t0
jal _print
move $a0 $t1
jal _print
move $a0 $t2
jal _print
lw $v1, 0($fp)
move $a0 $v1
jal _print
lw $v1, 4($fp)
move $a0 $v1
jal _print
lw $v1, 8($fp)
move $a0 $v1
jal _print
li $t3 0
move $v0 $t3
lw $s0, 12($sp)
lw $s1, 16($sp)
lw $s2, 20($sp)
lw $s3, 24($sp)
lw $s4, 28($sp)
lw $s5, 32($sp)
lw $s6, 36($sp)
lw $s7, 40($sp)
lw $ra, -4($fp)
lw $fp, 96($sp)
addu $sp, $sp, 104
j $ra

.text
.globl _halloc
_halloc:
li $v0, 9
syscall
j $ra

.text
.globl _print
_print:
li $v0, 1
syscall
la $a0, newl
 li $v0, 4
syscall
j $ra

.data
.align   0
newl:    .asciiz "\n"
.data
.align   0
str_er:  .asciiz " ERROR: abnormal termination\n" 


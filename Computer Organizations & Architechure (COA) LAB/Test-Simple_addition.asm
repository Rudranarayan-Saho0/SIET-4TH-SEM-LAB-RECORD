section .data
    num1 db 5        ; Define num1 as 5
    num2 db 10       ; Define num2 as 10
    result db 0      ; Placeholder for result

section .text
    global _start

_start:
    ; Load num1 into AL register
    mov al, [num1]
    ; Add num2 to AL register
    add al, [num2]
    ; Store result in memory
    mov [result], al

    ; Exit program
    mov eax, 1        ; syscall for exit
    xor ebx, ebx      ; return code 0
    int 0x80          ; interrupt to make syscall
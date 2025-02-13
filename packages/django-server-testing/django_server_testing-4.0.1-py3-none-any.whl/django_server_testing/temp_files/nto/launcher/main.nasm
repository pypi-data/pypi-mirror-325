; nasm main.nasm -o main.o -f win32 -s -O3
; ld main.o -o main.exe -m i386pe -s -O3 -LC:\Windows\SysWOW64 -lkernel32 -lshell32 --subsystem windows --enable-stdcall-fixup

global _start

extern _ShellExecuteA@24
extern _ExitProcess@4

section .text
_start:
	push 1
	push 0
	push parameters
	push path
	push 0
	push 0
	call _ShellExecuteA@24
	
	push eax
	call _ExitProcess@4

path: db ".\\source\\python\\pythonw.exe", 0
parameters: db ".\\source\\main.py", 0

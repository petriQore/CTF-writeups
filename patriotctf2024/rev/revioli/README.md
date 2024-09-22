gdb breakpoint just before comparing then print rdx register content

(gdb) b *0x00005555555555bb
(gdb) r
(gdb) x/s $rdx
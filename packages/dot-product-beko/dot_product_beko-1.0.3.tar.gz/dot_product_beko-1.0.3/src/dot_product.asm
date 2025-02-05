global dot_product

section .text
dot_product:
    vxorpd   ymm0, ymm0, ymm0       ; ymm0 = 0.0 (accumulator)

    mov     rcx, rdx
    shr     rcx, 2                 ; rcx = N / 4 (döngü sayısı)
    test    rcx, rcx
    jz      .tail

.loop:
    vmovupd ymm1, [rdi]            ; Load 4 doubles from x into ymm1
    vmovupd ymm2, [rsi]            ; Load 4 doubles from y into ymm2
    vfmadd231pd ymm0, ymm1, ymm2   ; ymm0 = (ymm1 * ymm2) + ymm0 (FMA)
    add     rdi, 32
    add     rsi, 32
    dec     rcx
    jnz     .loop

.tail:
    vextractf128 xmm1, ymm0, 1     
    vaddpd    xmm0, xmm0, xmm1     
    vhaddpd   xmm0, xmm0, xmm0     
    ret

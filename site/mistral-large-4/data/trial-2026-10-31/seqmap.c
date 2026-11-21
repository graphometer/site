// Test shim for the Large 4 trial: mark big read-only file maps sequential, so Linux keeps reading ahead when a model is larger than RAM.
#define _GNU_SOURCE
#include <dlfcn.h>
#include <sys/mman.h>
#include <stdio.h>
static void *(*real_mmap)(void *, size_t, int, int, int, off_t);
void *mmap(void *a, size_t n, int p, int f, int fd, off_t o) {
    if (!real_mmap) real_mmap = dlsym(RTLD_NEXT, "mmap");
    void *r = real_mmap(a, n, p, f, fd, o);
    if (r != MAP_FAILED && fd >= 0 && p == PROT_READ && n > (1UL << 30)) {
        madvise(r, n, MADV_SEQUENTIAL);
        fprintf(stderr, "seqmap: %zu GiB map marked sequential\n", n >> 30);
    }
    return r;
}
void *mmap64(void *a, size_t n, int p, int f, int fd, off_t o) { return mmap(a, n, p, f, fd, o); }

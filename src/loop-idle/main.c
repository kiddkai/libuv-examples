#include <uv.h>
#include <stdio.h>

int64_t counter = 0;
int64_t counter2 = 0;

void wait_for_a_while(uv_idle_t* handle) {
  counter++;

  printf("Calling Idle\n");

  if (counter >= 2) {
    uv_idle_stop(handle);
  }
}

void wait_for_a_while2(uv_idle_t* handle) {
  counter2++;

  printf("Calling Idle 2\n");

  if (counter2 >= 2) {
    uv_idle_stop(handle);
  }
}

int main() {
  uv_idle_t idler;
  uv_idle_t idler2;

  uv_idle_init(uv_default_loop(), &idler);
  uv_idle_init(uv_default_loop(), &idler2);
  uv_idle_start(&idler, wait_for_a_while);
  uv_idle_start(&idler2, wait_for_a_while2);

  printf("Idling...\n");
  uv_run(uv_default_loop(), UV_RUN_DEFAULT);

  uv_loop_close(uv_default_loop());
  return 0;
}

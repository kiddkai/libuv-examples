#include <uv.h>
#include <stdio.h>

int counter = 0;

void one_time_callback(uv_timer_t *handle) {
  printf("one time timer triggered\n");
  counter++;

  if (counter > 20) {
    uv_timer_stop(handle);
  }
}

int main() {
  uv_timer_t timer_req;

  uv_timer_init(uv_default_loop(), &timer_req);
  uv_timer_start(&timer_req, one_time_callback, 1000, 100);

  uv_run(uv_default_loop(), UV_RUN_DEFAULT);
  uv_loop_close(uv_default_loop());
  return 0;
}

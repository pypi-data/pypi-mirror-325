from test_function import test_function

from loog import log


def main():
    log("DEBUG test", "debug")
    log("INFO test")
    log("WARNING test", "warning")
    log("ERROR test", "error")
    log("CRITICAL test", "critical")

    log.log_off()
    log("log offed", "warning")

    log.log_on()
    log("log oned", "warning")

    test_function()


if __name__ == "__main__":
    log("Downloaded to ./downloads/6soo6/2월 리퀘 돈 주면 한 발 빼주는 일진 르르/2월 리퀘 돈 주면 한 발 빼주는 일진 르르_img19.png")
    log("A" * 100)
    log("Found image: ac-p1.namu.la/20250204sac/41d91c43ec97f1d0c807a5bdef13879015f06209aabf6a05ad333a3bf09f39d6.png?expires=")
    log("https://ac.namu.la/20250204sac/1a02c66c539abe029af063723e2c035197361ea4f2f22bfd9b890e43d778addb.png?expires=1738772684&key=ltz67t9anuKhmD5TxWBE6w&type=orig")
    log("a=b")
    # log.set_display_level("debug")
    # log.set_display_location(False)
    # log.set_loglevel_color("debug", "blue")
    # log.log_to_file()

    # log.create_custom_loglevel("info")
    # log.create_custom_loglevel("test", "green")
    # log.set_loglevel_color("test", "green")
    # log("TEST", "test")
    # log("abcdefghijklmnopqrstuvwxyz" * 20, "test")
    # log.set_display_level("test")

    # main()

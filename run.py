import click
import time
import json
import requests

@click.command()
@click.option("--host", default="0.0.0.0")
@click.option("-p", "--port", default=8000)
def main(host: str, port: int):
    start_time = time.perf_counter()

    click.echo(click.style("(⌐■_■)", bold=True, fg='black', bg='blue') + " Let's go  girls")
    r = requests.get(f"http://{host}:{port}/health")
    assert r.ok
    end_time = time.perf_counter()
    click.echo(click.style("(⌐■_■)", bold=True, fg='black', bg='blue') + fpose" Finished in {end_time - start_time}"))


if __name__ == "__main__":
    main()


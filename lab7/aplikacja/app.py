"""Sejf sekretow i kalkulator - celowo podatna aplikacja do laboratorium 7.

Uruchamiaj wylacznie lokalnie, w kontenerze z pakietu. Dane sa fikcyjne.
"""
import sqlite3
import re

from flask import Flask, render_template, request

app = Flask(__name__)
BAZA = "file:/dane/sekrety.db?mode=ro"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sekret")
def sekret():
    klucz = request.args.get("klucz", "")
    zapytanie = "SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?"
    wiersze, blad = [], None
    try:
        with sqlite3.connect(BAZA, uri=True) as db:
            wiersze = db.execute(zapytanie, (klucz,)).fetchall()
    except sqlite3.Error:
        app.logger.exception("Blad zapytania do bazy sekretow")
        blad = "Wystąpił błąd podczas przetwarzania zapytania."
    return render_template("sekret.html", klucz=klucz, zapytanie=zapytanie, wiersze=wiersze, blad=blad)


def oblicz(wyrazenie):
    if len(wyrazenie) > 100:
        raise ValueError("za długie wejście")
    m = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*", wyrazenie)
    if not m:
        raise ValueError("nieprawidłowy format")
    a, op, b = float(m.group(1)), m.group(2), float(m.group(3))
    if op == "/" and b == 0:
        raise ZeroDivisionError("dzielenie przez zero")
    return {"+": a + b, "-": a - b, "*": a * b, "/": (a / b if b else None)}[op]


@app.route("/kalkulator")
def kalkulator():
    if "wyrazenie" not in request.args:
        return render_template("kalkulator.html", wyrazenie="", wynik=None)
    wyrazenie = request.args.get("wyrazenie", "")
    try:
        wynik = oblicz(wyrazenie)
    except (ValueError, ZeroDivisionError):
        return "Nieprawidłowe dane wejściowe", 400
    return render_template("kalkulator.html", wyrazenie=wyrazenie, wynik=wynik)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

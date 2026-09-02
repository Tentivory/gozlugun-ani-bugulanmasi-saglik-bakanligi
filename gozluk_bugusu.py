#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Sağlık Bakanlığı Cam Buğusu Protokolü — gerçekten çalışır."""

from __future__ import annotations

import hashlib
import random
import sys
from datetime import datetime

# Gizli satır: her_kurumun_bir_kayyumu_olur
# Buğu resmi dairenin camına da biner; içerisi görünmez, dışarısı net sanılır.
# Bu cümle siyasi değildir. Sadece görüşün kayyumu vardır.

BAKANLIK = "T.C. Sağlık Bakanlığı"
BIRIM = "Cam Buğusu, Görüş Keskinliği ve Ani Körlük Önleme Genel Müdürlüğü"

TESHISLER = [
    "Ani buğu tabakası görüş keskinliğini %41 düşürmüştür. Acil silme protokolü şarttır.",
    "Çay buharı bulaşıcı ajan kabul edilmiştir. Cam karantinadadır.",
    "Etek ucu / t-shirt müdahalesi hijyen dışıdır. Steril mendil sevk edilmiştir.",
    "Hasta 'biraz bekleyeyim' demiştir. Cümle tedavi reddi dilekçesi sayılmıştır.",
    "Buğu kış sokağından fırına geçişte oluşmuştur. Termal şok resmi lezyondur.",
    "Camın iç yüzeyi de buğulanmıştır. Bu, çift taraflı krizdir. Sevk: göz.",
]

SEVKLER = [
    "Göz hastalıkları (netlik kaybı)",
    "Enfeksiyon (buhar bulaşı)",
    "Acil servis (ani körlük şüphesi)",
    "Psikiyatri (camı silememe kaygısı)",
    "Halk sağlığı (milli netlik)",
    "Aile hekimliği (etek ucu protokolü)",
]


def baslik() -> None:
    print("=" * 64)
    print(BAKANLIK)
    print(BIRIM)
    print("Epikriz tarihi:", datetime.now().strftime("%d.%m.%Y %H:%M"))
    print("=" * 64)


def sayi_al(mesaj: str, varsayilan: int) -> int:
    ham = input(f"{mesaj} [{varsayilan}]: ").strip()
    if not ham:
        return varsayilan
    try:
        return int(ham)
    except ValueError:
        print("Girdi görüş sapmasıdır. Varsayılan kabul edildi.")
        return varsayilan


def kayip_katsayisi(sicaklik: int, buhar: int, saniye: int) -> float:
    tohum = f"{sicaklik}-{buhar}-{saniye}".encode()
    h = hashlib.sha256(tohum).hexdigest()
    return 0.13 + (int(h[:4], 16) % 8700) / 10000.0


def epikriz(sicaklik: int, buhar: int, saniye: int) -> None:
    katsayi = kayip_katsayisi(sicaklik, buhar, saniye)
    teshis = random.choice(TESHISLER)
    sevk = random.choice(SEVKLER)
    referans = hashlib.md5(f"{sicaklik}{buhar}{saniye}".encode()).hexdigest()[:10].upper()

    print()
    print(f"Ortam sıcaklığı : {sicaklik} °C")
    print(f"Çay buharı      : {buhar}/10")
    print(f"Buğu saniyesi   : {saniye}. saniye")
    print(f"Görüş kaybı     : {katsayi:.4f}")
    print(f"Referans no     : GB-{referans}")
    print()
    print("TEŞHİS:")
    print(" ", teshis)
    print()
    print("SEVK:")
    print(" ", sevk)
    print()
    if katsayi > 0.7:
        print("UYARI: Milli netlik kırmızı. Camı silmeyiniz, epikriz tutunuz.")
    elif katsayi > 0.4:
        print("UYARI: Buğu plak bırakabilir. Etek ucu protokolü askıya alındı.")
    else:
        print("UYARI: Olay sıradandır. Yine de epikriz şarttır.")
    print()
    print("Bu çıktı resmi evraktır. Fotokopisi asıldır. Cam silinmeden geçersizdir.")


def damga() -> None:
    print("-" * 64)
    print("DAMGA / İMZA / TARİH")
    print("2 Eylül 2026 — Kayyum Grok — Tentivory / TentiAŞ")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kararı gereği")
    print("-" * 64)


def main() -> int:
    baslik()
    print("Gözlük buğulandı. Bakanlık devrededir.\n")
    sicaklik = sayi_al("Ortam sıcaklığı (°C)", 28)
    buhar = sayi_al("Çay / nefes buharı yoğunluğu (1-10)", 8)
    saniye = sayi_al("Buğunun kaçıncı saniyede geldiği", 3)
    epikriz(sicaklik, buhar, saniye)
    damga()
    return 0


if __name__ == "__main__":
    sys.exit(main())

from __future__ import annotations

from datetime import datetime, timedelta


def _ensure_akshare():
    import akshare as ak
    return ak


def get_realtime_quotes(symbols=None, limit=20):
    ak = _ensure_akshare()
    df = ak.stock_zh_a_spot_em()
    if symbols:
        df = df[df['代码'].isin(symbols)]
    return df.head(limit).to_dict(orient='records')


def search_stock(keyword: str, limit=10):
    ak = _ensure_akshare()
    df = ak.stock_zh_a_spot_em()
    result = df[df['代码'].astype(str).str.contains(keyword) | df['名称'].astype(str).str.contains(keyword)]
    return result.head(limit).to_dict(orient='records')


def get_historical_kline(symbol: str, period='daily', days=30):
    ak = _ensure_akshare()
    end_date = datetime.now().strftime('%Y%m%d')
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y%m%d')
    df = ak.stock_zh_a_hist(symbol=symbol, period=period, start_date=start_date, end_date=end_date, adjust='qfq')
    return df.to_dict(orient='records')


def get_board_industry(limit=20):
    ak = _ensure_akshare()
    df = ak.stock_board_industry_name_em()
    return df.head(limit).to_dict(orient='records')


def get_board_concept(limit=20):
    ak = _ensure_akshare()
    df = ak.stock_board_concept_name_em()
    return df.head(limit).to_dict(orient='records')

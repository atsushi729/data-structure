from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        """
        LFUキャッシュの初期化

        :param capacity: キャッシュの容量
        """
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}  # key: value
        self.key_to_freq = {}  # key: frequency
        self.freq_to_keys = defaultdict(OrderedDict)  # freq: keys (OrderedDictで順序を保持)

    def _update_freq(self, key: int):
        """
        キーのアクセス頻度を更新し、関連するデータ構造を調整します。

        :param key: 更新対象のキー
        """
        freq = self.key_to_freq[key]
        # 現在の頻度からキーを削除
        del self.freq_to_keys[freq][key]

        # 最小頻度が空になった場合、min_freqを更新
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # 頻度をインクリメントし、新しい頻度のリストにキーを追加
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        """
        指定されたキーの値を取得し、アクセス頻度を更新します。

        :param key: 取得対象のキー
        :return: キーに対応する値。キーが存在しない場合は -1 を返す。
        """
        if key not in self.key_to_val:
            return -1
        # アクセス頻度を更新
        self._update_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        """
        キーと値をキャッシュに追加します。キャッシュが容量を超える場合、
        最も使用頻度が低く、最も古いキーを削除します。

        :param key: 追加または更新するキー
        :param value: キーに対応する値
        """
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            # キーが既に存在する場合、値を更新し、頻度を更新
            self.key_to_val[key] = value
            self._update_freq(key)
            return

        if len(self.key_to_val) >= self.capacity:
            # 最小頻度のキーリストから最も古いキーを削除
            oldest_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[oldest_key]
            del self.key_to_freq[oldest_key]
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        # 新しいキーを追加
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1  # 新しいキーの頻度は1なので、min_freqを1に設定


# 使用例とテストケース
if __name__ == "__main__":
    # キャッシュ容量を2に設定
    cache = LFUCache(2)

    cache.put(1, 1)  # キャッシュ: {1=1}
    cache.put(2, 2)  # キャッシュ: {1=1, 2=2}
    print(cache.get(1))  # 出力: 1, キャッシュ: {1=1, 2=2}, freq(1)=2
    cache.put(3, 3)  # キー 2 を削除（freq=1 の最古）
    print(cache.get(2))  # 出力: -1 (キー 2 は削除された)
    print(cache.get(3))  # 出力: 3, キャッシュ: {1=1, 3=3}, freq(3)=2
    cache.put(4, 4)  # キー 1 を削除（freq=2 の最古）
    print(cache.get(1))  # 出力: -1 (キー 1 は削除された)
    print(cache.get(3))  # 出力: 3, キャッシュ: {3=3, 4=4}, freq(3)=3
    print(cache.get(4))  # 出力: 4, キャッシュ: {3=3, 4=4}, freq(4)=2
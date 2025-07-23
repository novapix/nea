interface CacheItem<T> {
  data: T;
  timestamp: number;
}

const CACHE_EXPIRY_MS = 5 * 60 * 1000; // 5 minutes

export function getCachedData<T>(key: string): T | null {
  const item = localStorage.getItem(key);
  if (!item) return null;
  
  const parsed: CacheItem<T> = JSON.parse(item);
  if (Date.now() - parsed.timestamp > CACHE_EXPIRY_MS) {
    localStorage.removeItem(key);
    return null;
  }
  
  return parsed.data;
}

export function setCachedData<T>(key: string, data: T): void {
  const item: CacheItem<T> = {
    data,
    timestamp: Date.now()
  };
  localStorage.setItem(key, JSON.stringify(item));
}

export function navigateSafely(to: string) {
  try {
    if (window.location.origin.startsWith('http')) {
      window.location.href = to;
    } else {
      window.location.reload();
    }
  } catch (error: unknown) {
    console.error('Navigation failed:', error);
    window.location.href = to;
  }
}

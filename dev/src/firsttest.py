import numpy as np

import matplotlib
matplotlib.use('Agg')   # 非対話環境でも描画可能にする（ファイル出力用）
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 1001)
h = 1e-5
num_deriv = (np.sin(x + h) - np.sin(x - h)) / (2*h)
analytical = np.cos(x)
error = np.abs(num_deriv - analytical)

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(x, analytical, label='analytical (cos x)')
plt.plot(x, num_deriv, '--', label='numerical derivative')
plt.legend()
plt.title('Derivative comparison')

plt.subplot(1,2,2)
plt.plot(x, error)
plt.title('Absolute error')
plt.ylim(0, np.max(error)*1.1)
plt.tight_layout()
plt.show()
plt.tight_layout()
plt.savefig('derivative_comparison.png', dpi=150)   # 画像として保存
# plt.show()  # 削除またはコメントアウト
print("max error:", np.max(error))





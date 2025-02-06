# matplotlib-radar

Feature-rich generation of radar chart based on matplotlib.

## Quick start

Install package with `pip install matplotlib-radar`.

Example code to generate radar chart:

```python
from matplotlib_radar import radar_chart
import numpy as np

radar_chart(
    label=["A", "B", "C", "D", "E"],
    data={"Sample 1": np.random.rand(5), "Sample 2": np.random.rand(5), "Sample 3": np.random.rand(5)},
    rotation=5,
    title="Radar chart with multiple samples",
)
```


![Example radar chart](./docs/source/_static/image/example-radar-chart.jpg)

For more plotting examples, check out the vignette notebook in the documentation.

## Development

```bash
# Clone repo
git clone https://github.com/harryhaller001/matplotlib-radar
cd matplotlib-radar

# Setup virtualenv
python3 -m virtualenv venv
source venv/bin/activate

# Install dependencies and setup precommit hook
make install

# Run all checks
make format
make testing
make typing
make build
```

## License

MIT license

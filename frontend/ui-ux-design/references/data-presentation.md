# Data presentation

Use for tables, charts, metrics, filtering, selection, and live or large datasets. Choose a representation for the question and required precision, not to make a screen look like a dashboard.

## Establish what the data means

Make the entity, measure, units, time range, aggregation, and comparison clear. Distinguish an absolute difference from a percentage or percentage-point change. A percentage needs a meaningful denominator; a trend needs a defined period and baseline.

Do not substitute zero for unknown or missing data. Separate no records, no matches, unavailable data, a failed query, and a genuine zero. Show sample data as sample data. Do not invent positive trends or plausible totals to complete a composition.

Precision should fit the decision. Consistent rounding aids comparison, but rounding must not erase meaningful distinctions. Explain estimated, sampled, partial, or stale values where those qualifications affect interpretation. Keep exact values accessible when needed for verification or action.

## Choose the smallest useful representation

| Need | Often useful | Watch for |
| --- | --- | --- |
| Find or compare exact records | Table or structured list | Lost column meaning, hidden values, unclear row actions |
| Compare category magnitudes | Bar or dot plot | Arbitrary order and misleading baseline |
| Understand change over time | Line or appropriate interval plot | Unequal time spacing, missing periods, false continuity |
| See distribution or variability | Histogram, box plot, or individual observations | Hidden sample size and misleading aggregation |
| Understand a part of a whole | Labeled bars, stacked bars, or a simple pie/donut | Too many similar segments and unclear denominator |
| Understand one important result | Value with units and meaningful context | Decorative KPI tiles without a decision to support |

These are starting points, not mandatory mappings. Use the representation that supports the actual comparison. Prefer a table over a chart when the user primarily needs lookup, editing, or precise reconciliation.

## Make charts honest and readable

Use scales that match the visual encoding. Bars usually need a zero baseline because length represents magnitude. A line chart can use a narrower range when the axis and context make the choice clear. Explain logarithmic scales, broken axes, and incomparable time windows rather than letting the appearance imply a false comparison.

Use sequential color for ordered magnitude, diverging color around a meaningful midpoint, and categorical color for distinct groups. Add labels, patterns, symbols, or other cues where color alone would make interpretation unreliable. Do not use danger colors just to make an ordinary series dramatic.

Direct labels can reduce the need for a legend. A legend helps when series identity is not otherwise clear; place it close enough to use. Label units and time granularity. Avoid decorative gradients, three-dimensional effects, and heavy gridlines that compete with the values.

Tooltips can expose detail but should not be the sole path to essential information. Consider keyboard and touch access, persistence while inspecting content, and what happens near the viewport edge. A crosshair is useful only when its relationship to the displayed values is clear.

Provide a meaningful accessible equivalent. A short text alternative can identify the visualization, while a summary and structured detail convey its information. A chart title alone may not explain the finding, and a large raw export alone may not communicate the overall pattern. See [WAI complex-image guidance](https://www.w3.org/WAI/tutorials/images/complex/) for web alternatives.

## Tables support work as well as reading

Keep headers associated with values and use alignment appropriate to the content. Choose columns for the task, not to fill available width. Make units, truncation, sort state, and row actions clear. Sticky headers and frozen columns help when they leave enough working space and do not obscure focus.

Add sorting where ordering supports a real task, rather than requiring every table to sort. Distinguish a sort from a filter or server query. For sortable web headers, expose direction with appropriate semantics. Sorting should not unexpectedly discard selection or make focus disappear.

When selecting records, distinguish selected rows on this page from all matching records. Bulk actions need visible scope and honest progress or failure reporting. After editing or deleting a row, preserve a logical focus position and explain partial failure rather than reporting universal success.

## Filtering, live data, and scale

Show active filters and provide a practical way to clear them. Keep filter scope and query scope understandable. When refresh is expensive or changes the working set substantially, an explicit apply action can be clearer than automatic refresh; immediate filtering can suit quick exploration. Preserve prior results during pending work when useful, without presenting them as the new result.

Live updates should not reorder a working list under the pointer or erase selection without warning. Consider pausing updates, showing a new-data indicator, or applying changes at a predictable point. Display freshness when decisions depend on it. Announce meaningful status, not every changing number.

For large datasets, distinguish rendering optimization from analytical transformation. Aggregation, sampling, and downsampling can alter the visible story; disclose the method when it affects interpretation and provide detail access when needed. Pagination and virtualization preserve different aspects of navigation and comparison. Do not choose them from a fixed row-count threshold.

Verify with missing values, a legitimate zero, long category names, a large outlier, changed filters during loading, and partial failure. A chart with tidy sample data is weak evidence of a usable data interface.

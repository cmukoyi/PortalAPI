import requests

url = "https://test.scopemlog.net/api/public/policy/17130603A001/17130603A001_RENAMED009"

payload = ""
headers = {
  'Authorization': 'bearer tklsUEycRs8CS2K0PyI29HAnI_Tej0OHpurDlDe7ABY9mYAigs5amjzUoUWWq1tlRSr8g1z1lkT3Y4J7Galbt4ZcEctLPJlx39DG2W4lpEkos8kXCxgpw3iXyr9Py_Ta0wjqws5vWCKgpMO9VLrxFsLoxdY9et-FM2OiZWkluvSbPbBv-w5OoAVrrkHG15im7Om7sFSAyaEIqV4E1zCkoM6K-ioufX-ivSkyAD2toTn8kakDI-SrO8hmVY1zgACo_dBfNsbs3KfDZmUreh88nBlIUTBjKsL9Lt7gkKFA__aI4Aj8HSTLckWI3QKADHRG57WmguE8UDj8bWJdND4_khDu36v9tsYxohH5UQOMCjXZkbusUrgd0vVesnNP0sZ-ZkHyQ-wnzNQ_vj0qOiaYWS6La2fdOollhcja5XlbUrN8cg-9lJIOCBCt2yzUwo8XnlpCKyDBLWLC2OPVOy8Nm-Q8wQqJHCPiIDHXraQMitzpYhxchhpRPkTHEysM4EqBW3OpomwJa3NZ6fy2aCUQ7jl2TKyG9TcAa99jQ4WlYHZ5yxWfMtt46Kmf6eU7T8O00Q89FKWqSBwnYF_ETfDWsyYT5fS_WsGxiU504Gmo_xOv4i1ynWkKh8OuTAcPUvwVGAgHFi7jlxJ5fu5u_8DzUGD-IjF7F_RmR6QGO6mkCA8LjQ5ccRx_pZ37P2tKQM7PDvyi2AeFwkKNIXRuB0fi299XFyINi1G2HtczcO9ffRtat03dPDUtkOZZ4yJPk6xFTxsvtaTMRdSePqwvYxxnMzsJ-at2posUvSNTruuEotEN2atUgWDKrzUx3sfTuVAn4Lfb4OlkgMhNieV-mmjmtGnYTB4UpATQ2Mg8sBFPzZ2Hay08ve9gv70puBt74GawdfeRIS4lFHl7hzJqVhb7sj0OHWV260f_V-_uigaypL88XcdY-ao4a1b6_njbtlomY1ixgwRxiClnfdNIy3rFZPd87dGvncTxHLgeANC5Ww1x_-GyH2O0izOZXl8joCAADb8EhZ5L19SvjLebPRyUN7KH2YrTXMNtTH5GE6cfLAWAH5vDaY73IBnDDXfju7LlqaXT6mW3h17MMdydvyGAF_zn7dI1QbxyHD_s9TDhGxfSRXNWNMFIK2jQwpz6Ur28OcHlW-XDWEpY-VJO-Mil1FVOftzPMVSYi1iSLc2aAjj4symTY3_UjUQt0SsTRGXoSUstE8V3OR8X3X_-5a8PY2ZZNQdDEYG0vVJwnFRHjeArpQI5Bh6ZyXQlljB0PZ8BjdUIDQ494Sxj66FVT9az6um8GPrLC2dcVnhiZ-I927ZuhUf6op_c5Ch6ehtVc0z7_s1ClrKE9J5KapjsCImbG-p7_CiqjeFEGiRXPPu4KskAHMTDlKJMmEVomZza6HIZ4FMlhwQ2k9M2f1EZOCVIyH5jFkuMqCyMoWwezkyXvFDZp9sEaEHbL5gyJde6o5KgRmZuOZZlpdwx_uyx9BOXiXs3Nc4tvfaCF1kwGvXMOAu-2VzKsXOV24wgVA92mGnJW86i0SA8wvFjVdLGNzcgR5lE9zsU3WuKWdryBHDvOgRAqqLVgmx2iwMpcUPItzxLhKyMyBu88VZmAAmWH2uAyXZ4jweOQFELbN_pAsvzV7WnH3pSi0f9Ta8_8BVd80FpIrw3rrYpnNzoYyvE5jPwxqWBhmYummoX6iMVEXGw15wMzkKCsKTjRp--mJtSkRWQNaxb0lK70GRYm-qMWWgTuEK3nGx2VVthganUw2U5nhFP7fKhGvdzHD6WdCY3fJz4gN5yFzNKKqcNF5jwc89PPS_6rU7jjDIJUTE5oK-Cw5q7u1gvsemHISIsdcUDa4Q2kSmPEZbbwUQcjnfEXNNprDUtpDyyawzCY8FmodDnqISnpMxsKa4uLgQLoGWpf6nI'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

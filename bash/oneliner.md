# Bash snippets

## Trimming stuff with awk and sed

```bash
$ acpi
Battery 0: Unknown, 100%
```

```bash
$ acpi | sed s'\,\ \'g
Battery 0: Unknown  100%
```

```bash
$ acpi | sed s'\,\ \'g | awk -F " " '{print $4 " " $3}'
100% Unknown
```

```bash
$ acpi | sed s'\,\ \'g | awk -F " " '{print $4 " " $3}' |tr -d "abcdefghijklmnopqrstuvwxyz"
100% U
```

## Recursively removing spaces in filenames

```bash
find . -name "* *" | while read a ; do mv "${a}" "${a//\ /_}" ; done
```

package main

// #include <Python.h>
import "C"

import (
	"fmt"

	"github.com/golang/example/stringutil"
)

//export reversemsg
func reversemsg() *C.PyObject {
	fmt.Print(stringutil.Reverse("elpmaxe tset"))

	return C.Py_None
}

func main() {}

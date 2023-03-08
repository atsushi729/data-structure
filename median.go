package honorsclass

import (
	"errors"
	"math/big"

	"github.com/mrekucci/epi/lists"
)

var ErrSort = errors.New("MedianOfSorted: list isn't sorted")

var ErrNode = errors.New("MedianOfSorted: list doesn't contain node")

var ErrType = errors.New("MedianOfSorted: value is not of the type int")

func MedianOfSorted(l *lists.List, csn *lists.Node) (*big.Rat, error) {
	if l.Len() == 0 {
		return nil, nil
	}

	// Find the list length.
	len := 0
	cnt := 0
	for p, n := l.First(), l.First(); n != nil; p, n = n, n.Next() {
		if n == csn {
			if cnt++; cnt == 2 { // Cycle detected.
				break
			}
		}
		len++
		vp, okp := p.Data.(int)
		vn, okn := n.Data.(int)
		if !okp || !okn { // Check whether the type assertion is ok.
			return nil, ErrType
		}
		if vp > vn { // Check whether data are sorted.
			return nil, ErrSort
		}
	}
	if csn != nil && cnt == 0 {
		return nil, ErrNode
	}

	// Find the middle node(s).
	p, n := l.First(), l.First()
	for i := 0; n != nil && i < len/2; i++ {
		p, n = n, n.Next()
	}

	// Evaluate the median (we've already checked the type assertion for all values).
	if len%2 == 0 {
		return big.NewRat(int64(n.Data.(int)+p.Data.(int)), 2), nil
	}
	return big.NewRat(int64(n.Data.(int)), 1), nil
}
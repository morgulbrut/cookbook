package main

import (
	"image"
	"image/color"
	"image/png"
	"os"
	"sync"

	"github.com/fogleman/gg"
)

type UserParams struct {
	// 	StrokeRatio              float64
	DestWidth  int
	DestHeight int
	// 	InitialAlpha             float64
	// 	StrokeReduction          float64
	// 	AlphaIncrease            float64
	// 	StrokeInversionThreshold float64
	// 	StrokeJitter             int
	// 	MinEdgeCount             int
	// 	MaxEdgeCount             int
	// 	RotationJitter           float64
	// 	Shape                    string
}

type Sketch struct {
	UserParams // embed for easier access
	source     image.Image
	dc         *gg.Context
}

func main() {
	var params UserParams
	params.DestHeight = 1000
	params.DestWidth = 2000

	s := NewSketch(params)

	var wg sync.WaitGroup

	wg.Add(1)
	go paintSquare(50, 0, 50, color.RGBA{255, 255, 255, 255}, s, &wg)
	wg.Add(1)
	go paintSquare(100, 0, 50, color.RGBA{255, 0, 0, 255}, s, &wg)
	wg.Add(1)
	go paintSquare(150, 0, 50, color.RGBA{255, 255, 0, 255}, s, &wg)

	wg.Wait()

	saveOutput(s.Output(), "test.png")

}

func NewSketch(userParams UserParams) *Sketch {
	s := &Sketch{UserParams: userParams}

	canvas := gg.NewContext(s.DestWidth, s.DestHeight)
	canvas.SetColor(color.Black)
	canvas.DrawRectangle(0, 0, float64(s.DestWidth), float64(s.DestHeight))
	canvas.Fill()
	s.dc = canvas
	return s
}

func (s *Sketch) Output() image.Image {
	return s.dc.Image()
}

func paintCircle(x float64, y float64, r float64, c color.RGBA, s *Sketch, wg *sync.WaitGroup) {
	defer wg.Done()
	s.dc.SetColor(c)
	s.dc.DrawCircle(x, y, r)
	s.dc.Fill()

	s.dc.Stroke()
}

func paintSquare(x float64, y float64, r float64, c color.RGBA, s *Sketch, wg *sync.WaitGroup) {
	defer wg.Done()
	s.dc.SetColor(c)
	s.dc.DrawRoundedRectangle(x, y, r, r, r/10)
	s.dc.Fill()

	s.dc.Stroke()

}

func saveOutput(img image.Image, filePath string) error {
	f, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer f.Close()

	// Encode to `PNG` with `DefaultCompression` level
	// then save to file
	err = png.Encode(f, img)
	if err != nil {
		return err
	}

	return nil
}

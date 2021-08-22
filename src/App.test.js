import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders learn topics link", () => {
  render(<App />);
  const linkElement = screen.getByText(/learn topics/i);
  expect(linkElement).toBeInTheDocument();
});

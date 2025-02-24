def getNumberOfPanelsThatFitOnRoof(xRoof, yRoof, xPanel, yPanel):
    return max(
        _getNumberOfPanelsThatFitOnRoof(xRoof, yRoof, xPanel, yPanel),
        _getNumberOfPanelsThatFitOnRoof(xRoof, yRoof, yPanel, xPanel))

def _getNumberOfPanelsThatFitOnRoof(xRoof, yRoof, xPanel, yPanel):
    """
    This function returns the maximum number of panels that fit on
    a roof of the specified dimensions.
    It works by first calculating the amount of panels that fit in
    one row (horizontally) and in one column (vertically). We then
    multiply both of these numbers to get the number of panels that
    we can place next to each other on the roof while maintaining
    the same panel rotation. Lastly, we calculate how many
    90°-rotated-panels we can place on the remaining space and
    we add it to the count.
    """
    totalPanelsThatFit = _getPanelsThatFitWithoutRotating(
        xRoof, yRoof, xPanel, yPanel)
    # Check how many 90 degrees rotated panels fit in
    # remaining space on the right
    remainingHorizontalSpace = xRoof % xPanel
    panelsThatFitInRemainingColumn = _getPanelsThatFitWithoutRotating(
        remainingHorizontalSpace, yRoof, yPanel, xPanel)
    totalPanelsThatFit += panelsThatFitInRemainingColumn
    # Check how many 90 degrees rotated panels fit in
    # remaining space above
    remainingVerticalSpace = yRoof % yPanel
    panelsThatFitInRemainingRow = _getPanelsThatFitWithoutRotating(
        xRoof, remainingVerticalSpace, yPanel, xPanel)
    totalPanelsThatFit += panelsThatFitInRemainingRow

    return totalPanelsThatFit

def _getPanelsThatFitWithoutRotating(xRoof, yRoof, xPanel, yPanel):
    panelsPerRow = xRoof // xPanel
    panelsPerColumn = yRoof // yPanel
    return panelsPerRow * panelsPerColumn

print(getNumberOfPanelsThatFitOnRoof(2, 4, 1, 2))
print(getNumberOfPanelsThatFitOnRoof(3, 5, 1, 2))
print(getNumberOfPanelsThatFitOnRoof(2, 2, 1, 10))
print(getNumberOfPanelsThatFitOnRoof(5, 11, 1, 3))
print(getNumberOfPanelsThatFitOnRoof(1600, 1230, 137, 95))

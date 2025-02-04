from ImageUI import translations
from ImageUI import variables
from ImageUI import settings
from ImageUI import colors
from ImageUI import errors
from ImageUI import states
import numpy as np
import traceback
import cv2


def CalculateTextSize(Text:str, TextWidth:int, FontSize:float = settings.FontSize):
    """
    Calculates the size, font size and thickness for a given text.

    Parameters
    ----------
    Text : str
        The text to calculate the values for.
    TextWidth : float
        The maximum width of the text.
    FontSize : float
        The maximum font size.

    Returns
    -------
    tuple of (str, float, int, int, int)
        1. The text.
        2. The font size.
        3. The thickness.
        4. The width of the text.
        5. The height of the text.
    """
    try:
        CurrentFontSize = 1
        Textsize, _ = cv2.getTextSize(Text, settings.FontType, CurrentFontSize, 1)
        WidthCurrentText, HeightCurrentText = Textsize
        MaxCountCurrentText = 3
        while WidthCurrentText != TextWidth or HeightCurrentText > FontSize:
            CurrentFontSize *= min(TextWidth / Textsize[0], FontSize / Textsize[1])
            Textsize, _ = cv2.getTextSize(Text, settings.FontType, CurrentFontSize, 1)
            MaxCountCurrentText -= 1
            if MaxCountCurrentText <= 0:
                break
        Thickness = round(CurrentFontSize * 2)
        if Thickness <= 0:
            Thickness = 1
        return Text, CurrentFontSize, Thickness, Textsize[0], Textsize[1]
    except:
        errors.ShowError("Elements - Error in function CalculateTextSize.", str(traceback.format_exc()))
        return "", 1, 1, 100, 100


def Button(Text, X1, Y1, X2, Y2, Selected, FontSize, RoundCorners, TextColor, Color, HoverColor, SelectedColor, SelectedHoverColor):
    try:
        Text = translations.Translate(Text)
        if X1 <= states.MouseX * variables.Frame.shape[1] <= X2 and Y1 <= states.MouseY * variables.Frame.shape[0] <= Y2 and states.ForegroundWindow:
            Hovered = True
        else:
            Hovered = False
        if Selected == True:
            if Hovered == True:
                cv2.rectangle(variables.Frame, (round(X1 + RoundCorners / 2), round(Y1 + RoundCorners / 2)), (round(X2 - RoundCorners / 2), round(Y2 - RoundCorners / 2)), SelectedHoverColor, RoundCorners, cv2.LINE_AA)
                cv2.rectangle(variables.Frame, (round(X1 + RoundCorners / 2), round(Y1 + RoundCorners / 2)), (round(X2 - RoundCorners / 2), round(Y2 - RoundCorners / 2)), SelectedHoverColor,  - 1, cv2.LINE_AA)
            else:
                cv2.rectangle(variables.Frame, (round(X1 + RoundCorners / 2), round(Y1 + RoundCorners / 2)), (round(X2 - RoundCorners / 2), round(Y2 - RoundCorners / 2)), SelectedColor, RoundCorners, cv2.LINE_AA)
                cv2.rectangle(variables.Frame, (round(X1 + RoundCorners / 2), round(Y1 + RoundCorners / 2)), (round(X2 - RoundCorners / 2), round(Y2 - RoundCorners / 2)), SelectedColor,  - 1, cv2.LINE_AA)
        elif Hovered == True:
            cv2.rectangle(variables.Frame, (round(X1 + RoundCorners / 2), round(Y1 + RoundCorners / 2)), (round(X2 - RoundCorners / 2), round(Y2 - RoundCorners / 2)), HoverColor, RoundCorners, cv2.LINE_AA)
            cv2.rectangle(variables.Frame, (round(X1 + RoundCorners / 2), round(Y1 + RoundCorners / 2)), (round(X2 - RoundCorners / 2), round(Y2 - RoundCorners / 2)), HoverColor,  - 1, cv2.LINE_AA)
        else:
            cv2.rectangle(variables.Frame, (round(X1 + RoundCorners / 2), round(Y1 + RoundCorners / 2)), (round(X2 - RoundCorners / 2), round(Y2 - RoundCorners / 2)), Color, RoundCorners, cv2.LINE_AA)
            cv2.rectangle(variables.Frame, (round(X1 + RoundCorners / 2), round(Y1 + RoundCorners / 2)), (round(X2 - RoundCorners / 2), round(Y2 - RoundCorners / 2)), Color,  - 1, cv2.LINE_AA)
        Text, FontSize, Thickness, Width, Height = CalculateTextSize(Text, round((X2 - X1)), FontSize)
        cv2.putText(variables.Frame, Text, (round(X1 + (X2 - X1) / 2 - Width / 2), round(Y1 + (Y2 - Y1) / 2 + Height / 2)), settings.FontType, FontSize, TextColor, Thickness, cv2.LINE_AA)
        if X1 <= states.MouseX * variables.Frame.shape[1] <= X2 and Y1 <= states.MouseY * variables.Frame.shape[0] <= Y2 and states.LeftClicked == False and states.LastLeftClicked == True:
            return True, states.LeftClicked and Hovered, Hovered
        else:
            return False, states.LeftClicked and Hovered, Hovered
    except:
        errors.ShowError("Elements - Error in function Button.", str(traceback.format_exc()))
        return False, False, False
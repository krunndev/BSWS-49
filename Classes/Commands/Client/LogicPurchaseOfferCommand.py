import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
from Classes.ByteStream import ByteStream
import random
from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Files.Classes.Skins import Skins
from Classes.Files.Classes.Pins import Pins
from Static.StaticData import StaticData
#from Classes.Logic.LogicStarrDropData import starrDropOpening
from time import time
import csv
OwnedPinsLatest = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687]
OwnedThumbnailsLatest = [60, 61, 63, 64, 69, 70, 72, 73, 76, 77, 78, 79, 83, 84]

OwnedBrawlersLatest = {
        0: {'CardID': 0, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        5: {'CardID': 20, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        11: {'CardID': 44, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        12: {'CardID': 48, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        14: {'CardID': 56, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        15: {'CardID': 60, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        16: {'CardID': 64, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        17: {'CardID': 68, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        20: {'CardID': 100, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        21: {'CardID': 105, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        23: {'CardID': 115, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        26: {'CardID': 130, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        28: {'CardID': 182, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        29: {'CardID': 188, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        30: {'CardID': 194, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        31: {'CardID': 200, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        32: {'CardID': 206, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        35: {'CardID': 224, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        36: {'CardID': 230, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        37: {'CardID': 236, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        38: {'CardID': 279, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        39: {'CardID': 296, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        40: {'CardID': 303, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        41: {'CardID': 320, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        42: {'CardID': 327, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        43: {'CardID': 334, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        44: {'CardID': 341, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        45: {'CardID': 358, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        46: {'CardID': 365, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        47: {'CardID': 372, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        48: {'CardID': 379, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        49: {'CardID': 386, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        50: {'CardID': 393, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        51: {'CardID': 410, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        52: {'CardID': 417, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        53: {'CardID': 427, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        54: {'CardID': 434, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        56: {'CardID': 448, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        57: {'CardID': 466, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        58: {'CardID': 474, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        59: {'CardID': 491, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        60: {'CardID': 499, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        62: {'CardID': 515, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        63: {'CardID': 523, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        64: {'CardID': 531, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        65: {'CardID': 539, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        
        66: {'CardID': 547, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        67: {'CardID': 557, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
}

def GetSkinPrice (O00O0O00O0O000O00, OO00OO0O0OO00O0OOOO00OO0O0OO00O0OO="Classes/Commands/Client/skins.txt"):
    def O0000OO0000OOOOO0 (OO0O00O000000O0O0 ):
        O000O0O00000O000O =0
        for OO00OO0O0OOOOOO0O in OO0O00O000000O0O0 :
            O000O0O00000O000O =O000O0O00000O000O *10 +ord (OO00OO0O0OOOOOO0O )-ord ('0')
        return O000O0O00000O000O
    def ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 (O0OOO0000000O00O0 ,O00OO0O00OO0OO000 =10 ,O0O0OOOO00O00O0OO =10 ):
        OOOOO0O0O0O0OOO00 =int (O0OOO0000000O00O0 ,O0O0OOOO00O00O0OO )if isinstance (O0OOO0000000O00O0 ,str )else O0OOO0000000O00O0
        OOO0OOO0OO0O0000O ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        OO00O0O000OO00O00 =""
        while OOOOO0O0O0O0OOO00 >0 :
            OOOOO0O0O0O0OOO00 ,O00000OOO0O0O0OOO =divmod (OOOOO0O0O0O0OOO00 ,O00OO0O00OO0OO000 )
            OO00O0O000OO00O00 +=OOO0OOO0OO0O0000O [O00000OOO0O0O0OOO ]
        return OO00O0O000OO00O00 [::-1 ]
    with open (f'{OO00OO0O0OO00O0OOOO00OO0O0OO00O0OO}')as OOOO0OOO00OO0OO00 :
        from csv import reader as oh ;OO00OO0O0OO00O0OO =0
        for O0OO000OOOOO00OOO in oh (OOOO0OOO00OO0OO00 ,delimiter =','):
            if (OO00OO0O0OO00O0OO in [ 0, 1]):OO00OO0O0OO00O0OO +=1
            else:
                if OO00OO0O0OO00O0OO -2 ==O00O0O00O0O000O00 :OO00O0O000OO00O00OO0B = int; return [O0000OO0000OOOOO0 (O0OO000OOOOO00OOO [ OO00O0O000OO00O00OO0B(ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789('I', O0O0OOOO00O00O0OO=OO00O0O000OO00O00OO0B("20", 16))) ]),O0000OO0000OOOOO0 (O0OO000OOOOO00OOO [ OO00O0O000OO00O00OO0B(ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789('H', O0O0OOOO00O00O0OO=OO00O0O000OO00O00OO0B("20", 16))) ])]
                if ""!=O0OO000OOOOO00OOO [0 ]:OO00OO0O0OO00O0OO +=1 
                
def GetPinPrice (O00O0O00O0O000O00, OO00OO0O0OO00O0OOOO00OO0O0OO00O0OO="Classes/Commands/Client/emotes.txt"):
    def O0000OO0000OOOOO0 (OO0O00O000000O0O0 ):
        O000O0O00000O000O =0
        for OO00OO0O0OOOOOO0O in OO0O00O000000O0O0 :
            O000O0O00000O000O =O000O0O00000O000O *10 +ord (OO00OO0O0OOOOOO0O )-ord ('0')
        return O000O0O00000O000O
    def ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 (O0OOO0000000O00O0 ,O00OO0O00OO0OO000 =10 ,O0O0OOOO00O00O0OO =10 ):
        OOOOO0O0O0O0OOO00 =int (O0OOO0000000O00O0 ,O0O0OOOO00O00O0OO )if isinstance (O0OOO0000000O00O0 ,str )else O0OOO0000000O00O0
        OOO0OOO0OO0O0000O ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        OO00O0O000OO00O00 =""
        while OOOOO0O0O0O0OOO00 >0 :
            OOOOO0O0O0O0OOO00 ,O00000OOO0O0O0OOO =divmod (OOOOO0O0O0O0OOO00 ,O00OO0O00OO0OO000 )
            OO00O0O000OO00O00 +=OOO0OOO0OO0O0000O [O00000OOO0O0O0OOO ]
        return OO00O0O000OO00O00 [::-1 ]
    with open (f'{OO00OO0O0OO00O0OOOO00OO0O0OO00O0OO}')as OOOO0OOO00OO0OO00 :
        from csv import reader as oh ;OO00OO0O0OO00O0OO =0
        for O0OO000OOOOO00OOO in oh (OOOO0OOO00OO0OO00 ,delimiter =','):
            if (OO00OO0O0OO00O0OO in [ 0, 1]):OO00OO0O0OO00O0OO +=1
            else:
                if OO00OO0O0OO00O0OO -2 ==O00O0O00O0O000O00 :OO00O0O000OO00O00OO0B = int; return [O0000OO0000OOOOO0 (O0OO000OOOOO00OOO [ OO00O0O000OO00O00OO0B(ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789('I', O0O0OOOO00O00O0OO=OO00O0O000OO00O00OO0B("20", 16))) ]),O0000OO0000OOOOO0 (O0OO000OOOOO00OOO [ OO00O0O000OO00O00OO0B(ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789('H', O0O0OOOO00O00O0OO=OO00O0O000OO00O00OO0B("20", 16))) ])]
                if ""!=O0OO000OOOOO00OOO [0 ]:OO00OO0O0OO00O0OO +=1 

class LogicPurchaseOfferCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload
        
        
    def getSkinsID():
        SkinsID = []
        with open('Classes/Commands/Client/skins.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[1].lower() != 'true':
                        SkinsID.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1
     
    def getPinsID():
        EmotesID = []
        with open('Classes/Commands/Client/emotes.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[1].lower() != 'true':
                        EmotesID.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["OfferIndex"] = calling_instance.readVInt()
        fields["Unk2"] = calling_instance.readDataReference()
        fields["CurrencyType"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        ShopData = StaticData.ShopData
        offer_index = fields["OfferIndex"] - 1

        if 0 <= offer_index < len(ShopData["Offers"]):
            offer = ShopData["Offers"][offer_index]

            # Списываем валюту
            if offer["Currency"] == 0:
                player_data["Gems"] -= offer["Cost"]
            elif offer["Currency"] == 1:
                player_data["Coins"] -= offer["Cost"]
            elif offer["Currency"] == 6:
                player_data["Blings"] -= offer["Cost"]
            elif offer["Currency"] == 5:
                player_data["ClubCoins"] -= offer["Cost"]

            # Обработка наград
            player_data["delivery_items"] = {'Boxes': []}
            box = {'Type': 0, 'Items': []}

            for reward in offer["Rewards"]:
                if reward.get("ItemType") == 3:
                    brawler_id = reward["BrawlerID"][1]
                    card_id = OwnedBrawlersLatest.get(brawler_id, {}).get('CardID', 0)

                    player_data["OwnedBrawlers"][brawler_id] = {
                        'CardID': card_id,
                        'Skins': [],
                        'Trophies': 0,
                        'HighestTrophies': 0,
                        'MasteryPoints': 0,
                        'MasteryClaimed': 0,
                        'PowerLevel': reward["Amount"],
                        'PowerPoints': 0, 
                        'State': 2
                    }
                    box['Type'] = 100
                    box['Items'].append({'Amount': reward["Amount"], 'DataRef': [16, brawler_id], 'RewardID': 1})

                elif reward.get("ItemType") == 19:
                    player_data["OwnedPins"].append(reward["Extra"])
                    item = {'Amount': 1, 'DataRef': [52, reward["Extra"]], 'RewardID': 11}
                    box['Type'] = 100
                    box['Items'].append(item)

                elif reward.get("ItemType") == 21:
                    brawlers = list(player_data["OwnedBrawlers"].keys())
                    brawler1 = int(random.choice(brawlers))
                    brawler2 = int(random.choice(brawlers))
                    brawler3 = int(random.choice(brawlers))

                    pin1 = random.choice(BrawlerPins[brawler1]['Common'])
                    while pin1 in player_data["OwnedPins"]:
                        pin1 = random.choice(BrawlerPins[brawler1]['Common'])

                    pin2 = random.choice(BrawlerPins[brawler2]['Common'])
                    while pin2 == pin1 or pin2 in player_data["OwnedPins"]:
                        pin2 = random.choice(BrawlerPins[brawler2]['Common'])

                    if random.randint(1, 3) == 3:
                        pin3 = random.choice(BrawlerPins[brawler3]['Epic'])
                        while pin3 in player_data["OwnedPins"]:
                            pin3 = random.choice(BrawlerPins[brawler3]['Epic'])
                    else:
                        pin3 = random.choice(BrawlerPins[brawler3]['Rare'])
                        while pin3 in player_data["OwnedPins"]:
                            pin3 = random.choice(BrawlerPins[brawler3]['Rare'])

                    player_data["OwnedPins"].append(pin1)
                    player_data["OwnedPins"].append(pin2)
                    player_data["OwnedPins"].append(pin3)

                    box['Type'] = 100
                    box['Items'].append({'Amount': 1, 'DataRef': [52, pin1], 'RewardID': 11})
                    box['Items'].append({'Amount': 1, 'DataRef': [52, pin2], 'RewardID': 11})
                    box['Items'].append({'Amount': 1, 'DataRef': [52, pin3], 'RewardID': 11})

                elif reward.get("ItemType") == 16:
                    player_data["Gems"] += reward["Amount"]
                    box['Type'] = 100
                    box['Items'].append({'Amount': reward["Amount"], 'DataRef': [0, 0], 'RewardID': 8})

                elif reward.get("ItemType") == 25:
                    player_data["OwnedThumbnails"].append(reward["Extra"])
                    box['Type'] = 100
                    box['Items'].append({'Amount': 1, 'DataRef': [28, reward["Extra"]], 'RewardID': 11})

                elif reward.get("ItemType") == 45:
                    player_data["Blings"] += reward["Amount"]
                    box['Type'] = 100
                    box['Items'].append({'Amount': reward["Amount"], 'DataRef': [0, 0], 'RewardID': 25})

                elif reward.get("ItemType") == 49:
                    #item = genStarDropReward(player_data)
                    box['Type'] = 100
                    box['Items'].append(item)

                elif reward.get("ItemType") == 50:
                    player_data["OwnedTitles"].append(reward["Extra"])
                    item = {'Amount': 1, 'DataRef': [71, 77],  'RewardID': 10}
                    box['Type'] = 100
                    box['Items'].append(item)

                elif reward.get("ItemType") == 1:
                    player_data["Coins"] += reward["Amount"]
                    box['Type'] = 100
                    box['Items'].append({'Amount': reward["Amount"], 'DataRef': [0, 0], 'RewardID': 7})

                elif reward.get("ItemType") == 4:
                    brawlerID = str(Skins.getBrawlerBySkin(self, reward["Extra"]))
                    for i,v in player_data["OwnedBrawlers"].items():
                        if str(i) == brawlerID:
                             v["Skins"].append(reward["Extra"])
                    box['Type'] = 100
                    item = {'Amount': 1, 'DataRef': [29, reward["Extra"]], 'RewardID': 9}
                    box['Items'].append(item)

            if box['Items']:
                player_data["delivery_items"]["Boxes"].append(box)

            if "PushasedOffers" not in player_data:
                player_data["PushasedOffers"] = []
            player_data["PushasedOffers"].append(offer["OfferID"])
            db_instance.updatePlayerData(player_data, calling_instance)
            fields["Socket"] = calling_instance.client
            fields["Command"] = {"ID": 203}
            fields["PlayerID"] = calling_instance.player.ID
            Messaging.sendMessage(24111, fields, cryptoInit)
            
        if fields["Unk2"][0] == 52:
            PinID = fields["Unk2"][1]
            Price = GetPinPrice(PinID)
           # вместо этого просто
            if fields["CurrencyType"] == 0:
            	player_data["Gems"] -= Price[0]
            elif fields["CurrencyType"] == 1:
            	player_data["Bling"] -= Price[1]
            else:
            	None
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [52, fields["Unk2"][1]],  'RewardID': 11}
            player_data["OwnedPins"].append(fields["Unk2"][1])
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)
            db_instance.updatePlayerData(player_data, calling_instance)
            fields["Socket"] = calling_instance.client
            fields["Command"] = {"ID": 203}
            fields["PlayerID"] = calling_instance.player.ID
            Messaging.sendMessage(24111, fields, cryptoInit)
            
        if fields["Unk2"][0] == 28:
            SkinID = fields["Unk2"][1]
            Price = GetSkinPrice(SkinID)
           # вместо этого просто
            if fields["CurrencyType"] == 0:
            	player_data["Gems"] -= 19
            elif fields["CurrencyType"] == 1:
            	player_data["Bling"] -= 750
            else:
            	None
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [28, fields["Unk2"][1]],  'RewardID': 11}
            player_data["OwnedThumbnails"].append(fields["Unk2"][1])
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)
            db_instance.updatePlayerData(player_data, calling_instance)
            fields["Socket"] = calling_instance.client
            fields["Command"] = {"ID": 203}
            fields["PlayerID"] = calling_instance.player.ID
            Messaging.sendMessage(24111, fields, cryptoInit)
            
        if fields["Unk2"][0] == 29:
            SkinID = fields["Unk2"][1]
            Price = GetSkinPrice(SkinID)
           # вместо этого просто
            if fields["CurrencyType"] == 0:
            	player_data["Gems"] -= 29
            elif fields["CurrencyType"] == 1:
            	player_data["Bling"] -= 1000
            else:
            	None
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [29, fields["Unk2"][1]],  'RewardID': 9}
            brawler = Skins.getBrawlerBySkin(self, fields["Unk2"][1])
            player_data["OwnedBrawlers"][f"{brawler}"]["Skins"].append(fields["Unk2"][1])
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)
            db_instance.updatePlayerData(player_data, calling_instance)
            fields["Socket"] = calling_instance.client
            fields["Command"] = {"ID": 203}
            fields["PlayerID"] = calling_instance.player.ID
            Messaging.sendMessage(24111, fields, cryptoInit)
       

    def getCommandType(self):
        return 519
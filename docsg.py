"""
Doc Signer
==========
Program to sign a document from an image file inserted in it.

@author Dr Mokira
@date   2022-22-05

"""
import os
import enum
from PIL import Image
from pdfrw import PdfReader, PdfWriter, PageMerge
from docx import Document
from docx.shared import Cm

__version__ = '0.0.1';
__author__  = 'Dr Mokira';


class dsg:
    # Python program to print
    # colored text and background
    class color:
        """ Colors class:reset all colors with colors.reset; two
            sub classes fg for foreground
            and bg for background; use as colors.subclass.colorname.
            i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
            underline, reverse, strike through,
            and invisible work with the main class i.e. colors.bold """

        RESET           = '\033[0m';
        BOLD            = '\033[01m';
        DISABLE         = '\033[02m';
        UNDERLINE       = '\033[04m';
        REVERSE         = '\033[07m';
        STRIKETHROUGH   = '\033[09m';
        INVISIBLE       = '\033[08m';

        class FG:
            BLACK       = '\033[30m';
            RED         = '\033[31m';
            GREEN       = '\033[32m';
            ORANGE      = '\033[33m';
            BLUE        = '\033[34m';
            PURPLE      = '\033[35m';
            CYAN        = '\033[36m';
            LIGHTGREY   = '\033[37m';
            DARKGREY    = '\033[90m';
            LIGHTRED    = '\033[91m';
            LIGHTGREEN  = '\033[92m';
            YELLOW      = '\033[93m';
            LIGHTBLUE   = '\033[94m';
            PINK        = '\033[95m';
            LIGHTCYAN   = '\033[96m';

        class BG:
            BLACK       = '\033[40m';
            RED         = '\033[41m';
            GREEN       = '\033[42m';
            ORANGE      = '\033[43m';
            BLUE        = '\033[44m';
            PURPLE      = '\033[45m';
            CYAN        = '\033[46m';
            LIGHTGREY   = '\033[47m';


    @staticmethod
    def log(cl, type, message):
        """ Function to make log in terminal. """
        print("{col}{fgc} {type} {reset} \t{message}".format(col=cl, fgc=dsg.color.FG.BLACK, type=type, reset=dsg.color.RESET, message=message));


    @staticmethod
    def printinfo(message):
        """ Function that is used to print infos in terminal. """
        dsg.log(dsg.color.BG.LIGHTGREY, 'INFO', message);


    @staticmethod
    def printwarn(message):
        """ Function that is used to print warnings in terminal. """
        dsg.log(dsg.color.BG.ORANGE, 'WARN', message);


    @staticmethod
    def printerr(message):
        """ Function that is used to print errors in terminal. """
        dsg.log(dsg.color.BG.RED, 'ERRO', message);

    @staticmethod
    def printsucc(message):
        """ Function that is used to print success message in terminal. """
        dsg.log(dsg.color.BG.GREEN, 'SUCC', message);


    @staticmethod
    def print_err_message(message):
        return "{col}{fgc} {message} {reset} \t".format(col=dsg.color.BG.RED, fgc=dsg.color.FG.BLACK, reset=dsg.color.RESET, message=message);


#######################################################################################################

    class DocType(enum.Enum):
        WORD = 0x001;
        PDF  = 0x002;


    @staticmethod
    def sign(din, dout, simg, doctype=None, pgn=-1, sdim=(128, 128), pos=(0, 0), color=(255, 255, 255)):
        """ Function that is used to sign a document.
            :args:
                din  [string] represents the location of the document to be signed.
                dout [string] represents the location to the signed document obtained after signing.
                simg [string] represents the image of the signature.
                doctype [dsg.DocType] Represents the type of document you want to sign.
                sdim   [tuple] represents the dimensions of the signature image.

            :return:
                True, if the signing operation is successful,
                False, else.
        """
        assert type(din)  is str, dsg.print_err_message("[din]  variable must be a string type.");
        assert type(dout) is str, dsg.print_err_message("[dout] variable must be a string type.");
        assert type(simg) is str, dsg.print_err_message("[simg] variable must be a string type.");
        assert doctype is None or type(doctype) is dsg.DocType, dsg.print_err_message("[doctype] variable must be a dsg.DocType type or None.");
        assert type(sdim) is tuple and len(sdim) == 2, dsg.print_err_message("[sdim] variable must be a tuple type with two elements (width, height).");
        assert type(pos) is tuple and len(pos) == 2, dsg.print_err_message("[pos] variable must be a tuple type with two elements (x, y).");
        assert type(pgn) is int, dsg.print_err_message("[sdim] variable must be an integer type.");

        resp = None;
        if doctype == dsg.DocType.PDF:
            resp = dsg._sign_pdf(din, dout, simg, pgn, sdim, pos, color);
        elif doctype == dsg.DocType.WORD:
            resp = dsg._sign_docx(din, dout, simg, pgn, sdim);
        else:
            dsg.printinfo("You must specify the type of document to be signed.");
            return False;

        if resp == True:
            dsg.printsucc(f"{din} is signed to {dout} successfully !");
            return True;
        else:
            dsg.printerr(f"{resp}");
            return False;


    @staticmethod
    def __adjust(p1, p2, x=36, y=36):
        info2 = PageMerge().add(p2);
        x2, y2, w2, h2 = info2.xobj_box;
        x += w2;
        y += h2;
        viewrect = (x, y, (w2 - x2 - 2 * x), (h2 - y2 - 2 * y));
        page     = PageMerge(p1).add(p2, viewrect=viewrect);
        return page.render();


    @staticmethod
    def _sign_pdf(din, dout, simg, pgn, sdim, pos, color):
        try:
            # We convert the signature to pdf doc, in first.
            img1 = Image.open(simg);
            im1 = img1.resize(sdim);
            im1 = im1.convert("RGB");
            im1.save('.sign.pdf', quality=95);

            watermark_file = '.sign.pdf';
            input_file     = din;
            output_file    = dout;

            # define the reader and writer objects
            reader_input  = PdfReader(input_file)
            writer_output = PdfWriter();

            # we open signature doc.
            watermark_input = PdfReader(watermark_file);
            watermark       = watermark_input.pages[0];

            # insert the signature image on the doc selected page.
            cp = len(reader_input.pages);
            pn = (cp - 1) if (pgn == -1 or pgn < 1 or pgn > cp) else (pgn - 1);

            # merger = PageMerge(reader_input.pages[pn]);
            # merger.add(watermark).render();
            page = reader_input.pages[pn];
            dsg.__adjust(page, watermark, pos[0], pos[1]);

            # write the modified content to disk
            writer_output.write(output_file, reader_input);
            if os.path.exists(watermark_file):
                # if the swap file is exists, delete it
                os.remove(watermark_file);

            return True;

        except Exception as e:
            return e.args[0];


    @staticmethod
    def _sign_docx(din, dout, simg, pgn, sdim):
        try:
            # we open doc
            document = Document(din);

            # we put 3 new paragraphs for ower signature
            p = document.add_paragraph();
            p = document.add_paragraph();
            p = document.add_paragraph();
            r = p.add_run();

            # we put the signature and save the data doc
            px = lambda cm: cm / 37.795275591;
            r.add_picture(simg, width=Cm(px(sdim[0])), height=Cm(px(sdim[1])));

            document.save(dout);
            return True;
        except Exception as e:
            return e.args[0];


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Program that use to merge an image to document page.");
    parser.add_argument('-t', '--type',
                            default='pdf',
                            dest='doctype',
                            help='Document type.',
                            choices=('pdf', 'word'),
                            required=True,
    );
    parser.add_argument('-i', '--in',
                            default='./input.pdf',
                            dest='din',
                            help='Input document.',
                            type=str,
                            required=True,
    );
    parser.add_argument('-n', '--page-number',
                            default=-1,
                            dest='page',
                            help='Page number.',
                            type=int,
    );
    parser.add_argument('-o', '--out',
                            default='./output.pdf',
                            dest='dout',
                            help='Output document.',
                            type=str,
                            required=True,
    );
    parser.add_argument('-s', '--simg',
                            default='./image.png',
                            dest='simg',
                            help='Signature image.',
                            type=str,
                            required=True,
    );
    parser.add_argument('-w', '--width',
                            default=150,
                            dest='width',
                            help='Width of signature image.',
                            type=int,
    );
    parser.add_argument('-x', '--margin-left',
                            default=10,
                            dest='x',
                            help='Margin left of signature image.',
                            type=int,
    );
    parser.add_argument('-y', '--margin-bottom',
                            default=10,
                            dest='y',
                            help='Margin bottom of signature image.',
                            type=int,
    );
    parser.add_argument('-r', '--red',
                            default=255,
                            dest='redc',
                            help='Background color red for signature image.',
                            type=int,
    );
    parser.add_argument('-g', '--green',
                            default=255,
                            dest='greenc',
                            help='Background color green for signature image.',
                            type=int,
    );
    parser.add_argument('-b', '--blue',
                            default=255,
                            dest='bluec',
                            help='Background color blue for signature image.',
                            type=int,
    );
    parser.add_argument('-e', '--height',
                            default=150,
                            dest='height',
                            help='Height of signature image.',
                            type=int,
    );
    args = parser.parse_args();
    dct  = dsg.DocType.PDF if args.doctype == 'pdf' else dsg.DocType.WORD;
    col  = (args.redc, args.greenc, args.bluec);
    dim  = (args.width, args.height);
    pos  = (args.x, args.y);
    pgn  = args.page;

    dsg.sign(args.din, args.dout, args.simg, dct, pgn, dim, pos, col);

    # print(f'The host is "{args.host}"')



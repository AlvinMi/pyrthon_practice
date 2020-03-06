# 这是在 stack overflow 上的
# from pathlib import Path

# class DisplayablePath(object):
#     display_filename_prefix_middle = '├──'
#     display_filename_prefix_last = '└──'
#     display_parent_prefix_middle = '    '
#     display_parent_prefix_last = '│   '

#     def __init__(self, path, parent_path, is_last):
#         self.path = Path(str(path))
#         self.parent = parent_path
#         self.is_last = is_last
#         if self.parent:
#             self.depth = self.parent.depth + 1
#         else:
#             self.depth = 0

#     @property
#     def displayname(self):
#         if self.path.is_dir():
#             return self.path.name + '/'
#         return self.path.name

#     @classmethod
#     def make_tree(cls, root, parent=None, is_last=False, criteria=None):
#         root = Path(str(root))
#         criteria = criteria or cls._default_criteria

#         displayable_root = cls(root, parent, is_last)
#         yield displayable_root

#         children = sorted(list(path
#                                for path in root.iterdir()
#                                if criteria(path)),
#                           key=lambda s: str(s).lower())
#         count = 1
#         for path in children:
#             is_last = count == len(children)
#             if path.is_dir():
#                 yield from cls.make_tree(path,
#                                          parent=displayable_root,
#                                          is_last=is_last,
#                                          criteria=criteria)
#             else:
#                 yield cls(path, displayable_root, is_last)
#             count += 1

#     @classmethod
#     def _default_criteria(cls, path):
#         return True

#     def displayable(self):
#         if self.parent is None:
#             return self.displayname

#         _filename_prefix = (self.display_filename_prefix_last
#                             if self.is_last
#                             else self.display_filename_prefix_middle)

#         parts = ['{!s} {!s}'.format(_filename_prefix,
#                                     self.displayname)]

#         parent = self.parent
#         while parent and parent.parent is not None:
#             parts.append(self.display_parent_prefix_middle
#                          if parent.is_last
#                          else self.display_parent_prefix_last)
#             parent = parent.parent

#         return ''.join(reversed(parts))

# # 使用
# paths = DisplayablePath.make_tree(Path('python_practice'))
# for path in paths:
#     print(path.displayable())


# ------------------------ #
import os, sys

PREFIX = ['└─ ', '├─ ']
INDENTION = ['│  ', ' '*4]

def tree(path , depth=1, flag=True, relation=[]):
    files = os.listdir(path)
    yield ''.join([PREFIX[not flag],os.path.basename(path),'\n'])

    depth += 1
    relation.append(flag)

    # for f in os.listdir(path):
    #     if not f.startswith('.'):
    #         yield f
    # 使用 os.walk 忽略掉隐藏文件，例如 .git
    # for root, dirs, files in os.walk(path):
    #     files = [f for f in files if not f[0] == '.']
    #     dirs[:] = [d for d in dirs if not d[0] == '.']
        # use files and dirs -- print
        # for file_name in files:  
        #     print(os.path.join(root, file_name) )
    
    for i in files:
        for j in relation:
            yield INDENTION[j]
        tempPath = os.path.join(path,i)

        if not os.path.isdir(tempPath):
            yield ''.join([PREFIX[i!=files[-1]], i, '\n'])
        else:
            for i in tree(tempPath,depth,i==files[-1],relation[:]):
                print(i,end='')
        
    
if __name__ == '__main__':
    for i in tree(sys.argv[1]):
        print(i,end='')

# usage 
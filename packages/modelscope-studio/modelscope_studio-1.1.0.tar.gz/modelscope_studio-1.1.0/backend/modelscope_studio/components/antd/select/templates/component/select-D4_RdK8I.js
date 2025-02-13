import { i as fe, a as U, r as me, g as he, w as P, b as _e } from "./Index-D3WkQiRc.js";
const k = window.ms_globals.React, ce = window.ms_globals.React.forwardRef, ae = window.ms_globals.React.useRef, ue = window.ms_globals.React.useState, de = window.ms_globals.React.useEffect, ee = window.ms_globals.React.useMemo, D = window.ms_globals.ReactDOM.createPortal, pe = window.ms_globals.internalContext.useContextPropsContext, N = window.ms_globals.internalContext.ContextPropsProvider, ge = window.ms_globals.antd.Select, xe = window.ms_globals.createItemsContext.createItemsContext;
var we = /\s/;
function be(e) {
  for (var t = e.length; t-- && we.test(e.charAt(t)); )
    ;
  return t;
}
var Ie = /^\s+/;
function ye(e) {
  return e && e.slice(0, be(e) + 1).replace(Ie, "");
}
var z = NaN, Ce = /^[-+]0x[0-9a-f]+$/i, ve = /^0b[01]+$/i, Ee = /^0o[0-7]+$/i, Re = parseInt;
function G(e) {
  if (typeof e == "number")
    return e;
  if (fe(e))
    return z;
  if (U(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = U(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = ye(e);
  var l = ve.test(e);
  return l || Ee.test(e) ? Re(e.slice(2), l ? 2 : 8) : Ce.test(e) ? z : +e;
}
var A = function() {
  return me.Date.now();
}, Se = "Expected a function", ke = Math.max, Oe = Math.min;
function Te(e, t, l) {
  var i, o, n, r, s, u, w = 0, g = !1, c = !1, x = !0;
  if (typeof e != "function")
    throw new TypeError(Se);
  t = G(t) || 0, U(l) && (g = !!l.leading, c = "maxWait" in l, n = c ? ke(G(l.maxWait) || 0, t) : n, x = "trailing" in l ? !!l.trailing : x);
  function a(m) {
    var I = i, R = o;
    return i = o = void 0, w = m, r = e.apply(R, I), r;
  }
  function _(m) {
    return w = m, s = setTimeout(p, t), g ? a(m) : r;
  }
  function f(m) {
    var I = m - u, R = m - w, j = t - I;
    return c ? Oe(j, n - R) : j;
  }
  function h(m) {
    var I = m - u, R = m - w;
    return u === void 0 || I >= t || I < 0 || c && R >= n;
  }
  function p() {
    var m = A();
    if (h(m))
      return y(m);
    s = setTimeout(p, f(m));
  }
  function y(m) {
    return s = void 0, x && i ? a(m) : (i = o = void 0, r);
  }
  function v() {
    s !== void 0 && clearTimeout(s), w = 0, i = u = o = s = void 0;
  }
  function d() {
    return s === void 0 ? r : y(A());
  }
  function E() {
    var m = A(), I = h(m);
    if (i = arguments, o = this, u = m, I) {
      if (s === void 0)
        return _(u);
      if (c)
        return clearTimeout(s), s = setTimeout(p, t), a(u);
    }
    return s === void 0 && (s = setTimeout(p, t)), r;
  }
  return E.cancel = v, E.flush = d, E;
}
var te = {
  exports: {}
}, W = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var je = k, Pe = Symbol.for("react.element"), Fe = Symbol.for("react.fragment"), Le = Object.prototype.hasOwnProperty, Ne = je.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, We = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ne(e, t, l) {
  var i, o = {}, n = null, r = null;
  l !== void 0 && (n = "" + l), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Le.call(t, i) && !We.hasOwnProperty(i) && (o[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) o[i] === void 0 && (o[i] = t[i]);
  return {
    $$typeof: Pe,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: Ne.current
  };
}
W.Fragment = Fe;
W.jsx = ne;
W.jsxs = ne;
te.exports = W;
var b = te.exports;
const {
  SvelteComponent: Ae,
  assign: q,
  binding_callbacks: V,
  check_outros: Me,
  children: re,
  claim_element: oe,
  claim_space: De,
  component_subscribe: J,
  compute_slots: Ue,
  create_slot: Be,
  detach: O,
  element: le,
  empty: X,
  exclude_internal_props: Y,
  get_all_dirty_from_scope: He,
  get_slot_changes: ze,
  group_outros: Ge,
  init: qe,
  insert_hydration: F,
  safe_not_equal: Ve,
  set_custom_element_data: ie,
  space: Je,
  transition_in: L,
  transition_out: B,
  update_slot_base: Xe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ye,
  getContext: Ke,
  onDestroy: Qe,
  setContext: Ze
} = window.__gradio__svelte__internal;
function K(e) {
  let t, l;
  const i = (
    /*#slots*/
    e[7].default
  ), o = Be(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = le("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      t = oe(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = re(t);
      o && o.l(r), r.forEach(O), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      F(n, t, r), o && o.m(t, null), e[9](t), l = !0;
    },
    p(n, r) {
      o && o.p && (!l || r & /*$$scope*/
      64) && Xe(
        o,
        i,
        n,
        /*$$scope*/
        n[6],
        l ? ze(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : He(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      l || (L(o, n), l = !0);
    },
    o(n) {
      B(o, n), l = !1;
    },
    d(n) {
      n && O(t), o && o.d(n), e[9](null);
    }
  };
}
function $e(e) {
  let t, l, i, o, n = (
    /*$$slots*/
    e[4].default && K(e)
  );
  return {
    c() {
      t = le("react-portal-target"), l = Je(), n && n.c(), i = X(), this.h();
    },
    l(r) {
      t = oe(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), re(t).forEach(O), l = De(r), n && n.l(r), i = X(), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(r, s) {
      F(r, t, s), e[8](t), F(r, l, s), n && n.m(r, s), F(r, i, s), o = !0;
    },
    p(r, [s]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, s), s & /*$$slots*/
      16 && L(n, 1)) : (n = K(r), n.c(), L(n, 1), n.m(i.parentNode, i)) : n && (Ge(), B(n, 1, 1, () => {
        n = null;
      }), Me());
    },
    i(r) {
      o || (L(n), o = !0);
    },
    o(r) {
      B(n), o = !1;
    },
    d(r) {
      r && (O(t), O(l), O(i)), e[8](null), n && n.d(r);
    }
  };
}
function Q(e) {
  const {
    svelteInit: t,
    ...l
  } = e;
  return l;
}
function et(e, t, l) {
  let i, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const s = Ue(n);
  let {
    svelteInit: u
  } = t;
  const w = P(Q(t)), g = P();
  J(e, g, (d) => l(0, i = d));
  const c = P();
  J(e, c, (d) => l(1, o = d));
  const x = [], a = Ke("$$ms-gr-react-wrapper"), {
    slotKey: _,
    slotIndex: f,
    subSlotIndex: h
  } = he() || {}, p = u({
    parent: a,
    props: w,
    target: g,
    slot: c,
    slotKey: _,
    slotIndex: f,
    subSlotIndex: h,
    onDestroy(d) {
      x.push(d);
    }
  });
  Ze("$$ms-gr-react-wrapper", p), Ye(() => {
    w.set(Q(t));
  }), Qe(() => {
    x.forEach((d) => d());
  });
  function y(d) {
    V[d ? "unshift" : "push"](() => {
      i = d, g.set(i);
    });
  }
  function v(d) {
    V[d ? "unshift" : "push"](() => {
      o = d, c.set(o);
    });
  }
  return e.$$set = (d) => {
    l(17, t = q(q({}, t), Y(d))), "svelteInit" in d && l(5, u = d.svelteInit), "$$scope" in d && l(6, r = d.$$scope);
  }, t = Y(t), [i, o, g, c, s, u, r, n, y, v];
}
class tt extends Ae {
  constructor(t) {
    super(), qe(this, t, et, $e, Ve, {
      svelteInit: 5
    });
  }
}
const Z = window.ms_globals.rerender, M = window.ms_globals.tree;
function nt(e, t = {}) {
  function l(i) {
    const o = P(), n = new tt({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? M;
          return u.nodes = [...u.nodes, s], Z({
            createPortal: D,
            node: M
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((w) => w.svelteInstance !== o), Z({
              createPortal: D,
              node: M
            });
          }), s;
        },
        ...i.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(l);
    });
  });
}
const rt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ot(e) {
  return e ? Object.keys(e).reduce((t, l) => {
    const i = e[l];
    return t[l] = lt(l, i), t;
  }, {}) : {};
}
function lt(e, t) {
  return typeof t == "number" && !rt.includes(e) ? t + "px" : t;
}
function H(e) {
  const t = [], l = e.cloneNode(!1);
  if (e._reactElement) {
    const o = k.Children.toArray(e._reactElement.props.children).map((n) => {
      if (k.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: s
        } = H(n.props.el);
        return k.cloneElement(n, {
          ...n.props,
          el: s,
          children: [...k.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(D(k.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: o
    }), l)), {
      clonedElement: l,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: r,
      type: s,
      useCapture: u
    }) => {
      l.addEventListener(s, r, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let o = 0; o < i.length; o++) {
    const n = i[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: s
      } = H(n);
      t.push(...s), l.appendChild(r);
    } else n.nodeType === 3 && l.appendChild(n.cloneNode());
  }
  return {
    clonedElement: l,
    portals: t
  };
}
function it(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const C = ce(({
  slot: e,
  clone: t,
  className: l,
  style: i,
  observeAttributes: o
}, n) => {
  const r = ae(), [s, u] = ue([]), {
    forceClone: w
  } = pe(), g = w ? !0 : t;
  return de(() => {
    var _;
    if (!r.current || !e)
      return;
    let c = e;
    function x() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), it(n, f), l && f.classList.add(...l.split(" ")), i) {
        const h = ot(i);
        Object.keys(h).forEach((p) => {
          f.style[p] = h[p];
        });
      }
    }
    let a = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var v, d, E;
        (v = r.current) != null && v.contains(c) && ((d = r.current) == null || d.removeChild(c));
        const {
          portals: p,
          clonedElement: y
        } = H(e);
        c = y, u(p), c.style.display = "contents", x(), (E = r.current) == null || E.appendChild(c);
      };
      f();
      const h = Te(() => {
        f(), a == null || a.disconnect(), a == null || a.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      a = new window.MutationObserver(h), a.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", x(), (_ = r.current) == null || _.appendChild(c);
    return () => {
      var f, h;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((h = r.current) == null || h.removeChild(c)), a == null || a.disconnect();
    };
  }, [e, g, l, i, n, o]), k.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...s);
});
function st(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function ct(e, t = !1) {
  try {
    if (_e(e))
      return e;
    if (t && !st(e))
      return;
    if (typeof e == "string") {
      let l = e.trim();
      return l.startsWith(";") && (l = l.slice(1)), l.endsWith(";") && (l = l.slice(0, -1)), new Function(`return (...args) => (${l})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function S(e, t) {
  return ee(() => ct(e, t), [e, t]);
}
function se(e, t, l) {
  const i = e.filter(Boolean);
  if (i.length !== 0)
    return i.map((o, n) => {
      var w;
      if (typeof o != "object")
        return t != null && t.fallback ? t.fallback(o) : o;
      const r = {
        ...o.props,
        key: ((w = o.props) == null ? void 0 : w.key) ?? (l ? `${l}-${n}` : `${n}`)
      };
      let s = r;
      Object.keys(o.slots).forEach((g) => {
        if (!o.slots[g] || !(o.slots[g] instanceof Element) && !o.slots[g].el)
          return;
        const c = g.split(".");
        c.forEach((p, y) => {
          s[p] || (s[p] = {}), y !== c.length - 1 && (s = r[p]);
        });
        const x = o.slots[g];
        let a, _, f = (t == null ? void 0 : t.clone) ?? !1, h = t == null ? void 0 : t.forceClone;
        x instanceof Element ? a = x : (a = x.el, _ = x.callback, f = x.clone ?? f, h = x.forceClone ?? h), h = h ?? !!_, s[c[c.length - 1]] = a ? _ ? (...p) => (_(c[c.length - 1], p), /* @__PURE__ */ b.jsx(N, {
          params: p,
          forceClone: h,
          children: /* @__PURE__ */ b.jsx(C, {
            slot: a,
            clone: f
          })
        })) : /* @__PURE__ */ b.jsx(N, {
          forceClone: h,
          children: /* @__PURE__ */ b.jsx(C, {
            slot: a,
            clone: f
          })
        }) : s[c[c.length - 1]], s = r;
      });
      const u = (t == null ? void 0 : t.children) || "children";
      return o[u] ? r[u] = se(o[u], t, `${n}`) : t != null && t.children && (r[u] = void 0, Reflect.deleteProperty(r, u)), r;
    });
}
function $(e, t) {
  return e ? /* @__PURE__ */ b.jsx(C, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function T({
  key: e,
  slots: t,
  targets: l
}, i) {
  return t[e] ? (...o) => l ? l.map((n, r) => /* @__PURE__ */ b.jsx(N, {
    params: o,
    forceClone: !0,
    children: $(n, {
      clone: !0,
      ...i
    })
  }, r)) : /* @__PURE__ */ b.jsx(N, {
    params: o,
    forceClone: !0,
    children: $(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
const {
  withItemsContextProvider: at,
  useItems: ut,
  ItemHandler: ft
} = xe("antd-select-options"), mt = nt(at(["options", "default"], ({
  slots: e,
  children: t,
  onValueChange: l,
  filterOption: i,
  onChange: o,
  options: n,
  getPopupContainer: r,
  dropdownRender: s,
  optionRender: u,
  tagRender: w,
  labelRender: g,
  filterSort: c,
  elRef: x,
  setSlotParams: a,
  ..._
}) => {
  const f = S(r), h = S(i), p = S(s), y = S(c), v = S(u), d = S(w), E = S(g), {
    items: m
  } = ut(), I = m.options.length > 0 ? m.options : m.default;
  return /* @__PURE__ */ b.jsxs(b.Fragment, {
    children: [/* @__PURE__ */ b.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ b.jsx(ge, {
      ..._,
      ref: x,
      options: ee(() => n || se(I, {
        children: "options",
        clone: !0
      }), [I, n]),
      onChange: (R, ...j) => {
        o == null || o(R, ...j), l(R);
      },
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ b.jsx(C, {
          slot: e["allowClear.clearIcon"]
        })
      } : _.allowClear,
      prefix: e.prefix ? /* @__PURE__ */ b.jsx(C, {
        slot: e.prefix
      }) : _.prefix,
      removeIcon: e.removeIcon ? /* @__PURE__ */ b.jsx(C, {
        slot: e.removeIcon
      }) : _.removeIcon,
      suffixIcon: e.suffixIcon ? /* @__PURE__ */ b.jsx(C, {
        slot: e.suffixIcon
      }) : _.suffixIcon,
      notFoundContent: e.notFoundContent ? /* @__PURE__ */ b.jsx(C, {
        slot: e.notFoundContent
      }) : _.notFoundContent,
      menuItemSelectedIcon: e.menuItemSelectedIcon ? /* @__PURE__ */ b.jsx(C, {
        slot: e.menuItemSelectedIcon
      }) : _.menuItemSelectedIcon,
      filterOption: h || i,
      maxTagPlaceholder: e.maxTagPlaceholder ? T({
        slots: e,
        setSlotParams: a,
        key: "maxTagPlaceholder"
      }) : _.maxTagPlaceholder,
      getPopupContainer: f,
      dropdownRender: e.dropdownRender ? T({
        slots: e,
        setSlotParams: a,
        key: "dropdownRender"
      }) : p,
      optionRender: e.optionRender ? T({
        slots: e,
        setSlotParams: a,
        key: "optionRender"
      }) : v,
      tagRender: e.tagRender ? T({
        slots: e,
        setSlotParams: a,
        key: "tagRender"
      }) : d,
      labelRender: e.labelRender ? T({
        slots: e,
        setSlotParams: a,
        key: "labelRender"
      }) : E,
      filterSort: y
    })]
  });
}));
export {
  mt as Select,
  mt as default
};
